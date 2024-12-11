import json
import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

@pytest.fixture
def sample_user():
    return User(username='testuser', email='test@example.com')

def test_health_check(client):
    """Teste da rota de saúde"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_create_user(client):
    """Teste de criação de usuário"""
    user_data = {
        'username': 'newuser',
        'email': 'newuser@example.com'
    }
    response = client.post('/users', 
                           data=json.dumps(user_data), 
                           content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['username'] == user_data['username']
    assert data['email'] == user_data['email']

def test_list_users(client, sample_user):
    """Teste de listagem de usuários"""
    # Adicionar usuário de exemplo
    with app.app_context():
        db.session.add(sample_user)
        db.session.commit()

    response = client.get('/users')
    assert response.status_code == 200
    
    users = json.loads(response.data)
    assert len(users) > 0
    assert any(user['username'] == sample_user.username for user in users)

def test_user_model(sample_user):
    """Teste do modelo de usuário"""
    assert sample_user.username == 'testuser'
    assert sample_user.email == 'test@example.com'
    
    user_dict = sample_user.to_dict()
    assert 'id' in user_dict
    assert user_dict['username'] == 'testuser'
    assert user_dict['email'] == 'test@example.com'

def test_create_user_duplicate(client):
    """Teste de criação de usuário duplicado"""
    user_data = {
        'username': 'duplicateuser',
        'email': 'duplicate@example.com'
    }
    
    # Primeira criação
    response1 = client.post('/users', 
                            data=json.dumps(user_data), 
                            content_type='application/json')
    assert response1.status_code == 201
    
    # Segunda criação (deve falhar)
    response2 = client.post('/users', 
                            data=json.dumps(user_data), 
                            content_type='application/json')
    assert response2.status_code == 400
