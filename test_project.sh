#!/bin/bash

# Cores para saída no terminal
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # Sem cor

# Função de log
log() {
    echo -e "${GREEN}[TESTE]${NC} $1"
}

# Função de erro
error() {
    echo -e "${RED}[ERRO]${NC} $1" >&2
}

# Verificar dependências
check_dependencies() {
    log "Verificando dependências..."
    
    local dependencies=("docker" "docker-compose" "kubectl" "minikube")
    local missing_deps=()

    for cmd in "${dependencies[@]}"; do
        if ! command -v "$cmd" &> /dev/null; then
            missing_deps+=("$cmd")
        fi
    done

    if [ ${#missing_deps[@]} -ne 0 ]; then
        error "Dependências faltando: ${missing_deps[*]}"
        exit 1
    fi
}

# Testar Docker Compose
test_docker_compose() {
    log "Testando Docker Compose..."
    
    docker-compose up -d
    
    if [ $? -ne 0 ]; then
        error "Falha ao iniciar serviços com Docker Compose"
        exit 1
    fi

    # Aguardar inicialização
    sleep 30

    # Verificar logs
    docker-compose logs

    # Testar conexão com Flask
    curl http://localhost:5000/health

    # Testar conexão com MySQL
    docker-compose exec mysql mysqladmin ping -h localhost

    docker-compose down
}

# Testar Kubernetes
test_kubernetes() {
    log "Testando Kubernetes..."
    
    # Iniciar Minikube
    minikube start --driver=docker

    # Aplicar manifestos
    kubectl apply -f k8s/

    # Aguardar inicialização dos pods
    kubectl get pods
    kubectl wait --for=condition=Ready pods --all --timeout=5m

    # Verificar serviços
    kubectl get services

    # Testar conexão (pode precisar de port-forward)
    kubectl port-forward service/flask-service 5000:5000 &
    sleep 10
    curl http://localhost:5000/health

    # Limpar
    minikube delete
}

# Testar aplicação Flask
test_flask_app() {
    log "Testando aplicação Flask..."
    
    cd src
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    # Executar testes unitários
    pytest tests/

    # Desativar ambiente virtual
    deactivate
}

# Função principal
main() {
    check_dependencies
    test_docker_compose
    test_flask_app
    test_kubernetes

    log "Todos os testes concluídos com sucesso! 🎉"
}

# Executar
main
