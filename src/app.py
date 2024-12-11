import os
import logging
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configurações de segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_secret_key')
app.config['ALLOWED_HOSTS'] = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'sqlite:///default.db'  # Fallback para SQLite se nenhuma URL for fornecida
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados
db = SQLAlchemy(app)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# Criar tabelas
@app.before_first_request
def create_tables():
    try:
        db.create_all()
        logger.info("Tabelas criadas com sucesso")
    except Exception as e:
        logger.error(f"Erro ao criar tabelas: {e}")

# Rota para listar usuários
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        logger.error(f"Erro ao listar usuários: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rota para adicionar usuário
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        new_user = User(
            username=data.get('username'),
            email=data.get('email')
        )
        db.session.add(new_user)
        db.session.commit()
        logger.info(f"Usuário {new_user.username} criado com sucesso")
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        logger.error(f"Usuário duplicado: {data.get('username')}")
        return jsonify({"error": "Usuário ou email já existente"}), 400
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao criar usuário: {e}")
        return jsonify({"error": "Erro ao criar usuário"}), 400

# Rota de saúde
@app.route('/health', methods=['GET'])
def health_check():
    try:
        # Verificar conexão com o banco de dados
        db.session.execute('SELECT 1')
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        logger.error(f"Falha na verificação de saúde: {e}")
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=int(os.getenv('PORT', 5000)), 
        debug=os.getenv('FLASK_DEBUG', 'False') == 'True'
    )
