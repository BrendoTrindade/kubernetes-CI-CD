import os
from app import app, db, User

def init_db():
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()

        # Adicionar usuários iniciais, se não existirem
        if not User.query.first():
            initial_users = [
                User(username='admin', email='admin@example.com'),
                User(username='user', email='user@example.com')
            ]
            
            for user in initial_users:
                db.session.add(user)
            
            db.session.commit()
            print("Banco de dados inicializado com usuários padrão.")
        else:
            print("Banco de dados já possui usuários.")

if __name__ == '__main__':
    init_db()
