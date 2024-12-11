#!/bin/bash

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python 3 não encontrado. Por favor, instale o Python 3."
    exit 1
fi

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Atualizar pip
pip install --upgrade pip

# Instalar dependências
pip install -r src/requirements.txt

# Copiar .env.example para .env se não existir
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Arquivo .env criado. Por favor, edite-o com suas configurações."
fi

# Configurar banco de dados (MySQL)
echo "Lembre-se de configurar seu banco de dados MySQL antes de iniciar a aplicação."
echo "Você pode usar o Docker Compose para iniciar o banco de dados:"
echo "docker-compose up mysql"

# Executar migrações (se aplicável)
# flask db upgrade

# Sugestão de próximos passos
echo ""
echo "Ambiente de desenvolvimento configurado com sucesso!"
echo "Próximos passos:"
echo "1. Ative o ambiente virtual: source venv/bin/activate"
echo "2. Configure suas variáveis de ambiente no arquivo .env"
echo "3. Inicie o banco de dados com Docker Compose"
echo "4. Execute a aplicação: flask run"
