#!/bin/bash

# Verificar dependências
check_dependencies() {
    echo "Verificando dependências..."
    
    # Docker
    if ! command -v docker &> /dev/null; then
        echo "Docker não encontrado. Por favor, instale o Docker."
        exit 1
    fi

    # Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        echo "Docker Compose não encontrado. Por favor, instale o Docker Compose."
        exit 1
    fi

    # Python
    if ! command -v python3 &> /dev/null; then
        echo "Python 3 não encontrado. Por favor, instale o Python."
        exit 1
    fi
}

# Configurar ambiente virtual
setup_venv() {
    echo "Configurando ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r src/requirements.txt
}

# Construir e iniciar containers
start_containers() {
    echo "Construindo e iniciando containers..."
    docker-compose up --build -d
}

# Executar migrações (se necessário)
run_migrations() {
    echo "Executando migrações..."
    docker-compose exec flask-app flask db upgrade
}

# Executar testes
run_tests() {
    echo "Executando testes..."
    docker-compose exec flask-app pytest tests/
}

# Exibir status
show_status() {
    echo "Serviços em execução:"
    docker-compose ps
    echo ""
    echo "Acesse a aplicação em: http://localhost"
}

# Função principal
main() {
    check_dependencies
    setup_venv
    start_containers
    run_migrations
    run_tests
    show_status
}

# Executar
main
