#!/bin/bash

# Script de configuração para o projeto DevOps

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python 3 não encontrado. Por favor, instale o Python 3."
    exit 1
fi

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r src/requirements.txt

# Configurar variáveis de ambiente
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Arquivo .env criado. Por favor, configure suas credenciais."
fi

# Inicializar banco de dados
python src/init_db.py

# Executar testes
pytest src/test_app.py

echo "Configuração concluída com sucesso!"
