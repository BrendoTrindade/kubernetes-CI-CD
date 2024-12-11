import unittest
import json
from app import app, db, User

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"status": "healthy"})

    def test_create_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        response = self.app.post('/users', 
                                 data=json.dumps(user_data), 
                                 content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        
        response_data = json.loads(response.data)
        self.assertEqual(response_data['username'], 'testuser')
        self.assertEqual(response_data['email'], 'test@example.com')

    def test_get_users(self):
        # Primeiro, cria um usuário
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        self.app.post('/users', 
                      data=json.dumps(user_data), 
                      content_type='application/json')

        # Então, busca os usuários
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        
        users = json.loads(response.data)
        self.assertTrue(len(users) > 0)
        self.assertEqual(users[0]['username'], 'testuser')

if __name__ == '__main__':
    unittest.main()
