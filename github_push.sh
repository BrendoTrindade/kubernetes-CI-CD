#!/bin/bash

# Cores para saída no terminal
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # Sem cor

# URL do repositório
REPO_URL="https://github.com/BrendoTrindade/kubernetes-CI-CD.git"

# Função de log
log() {
    echo -e "${GREEN}[GITHUB]${NC} $1"
}

# Função de erro
error() {
    echo -e "${RED}[ERRO]${NC} $1" >&2
}

# Verificar se o Git está instalado
if ! command -v git &> /dev/null; then
    error "Git não está instalado. Por favor, instale o Git."
    exit 1
fi

# Inicializar repositório Git (se não estiver inicializado)
if [ ! -d .git ]; then
    log "Inicializando repositório Git..."
    git init
fi

# Configurar identidade do Git (substitua com seus dados)
git config user.name "Brendo Trindade"
git config user.email "brendo.trindade@example.com"

# Adicionar todos os arquivos, exceto secrets
log "Preparando arquivos para commit..."
git add .
git reset k8s/mysql-secrets.yaml

# Verificar se há mudanças para commitar
if [[ -n $(git status -s) ]]; then
    # Fazer commit
    log "Criando commit..."
    git commit -m "Projeto DevOps Flask: Microserviços com Docker, Kubernetes e CI/CD"
else
    log "Nenhuma mudança para commitar."
fi

# Adicionar repositório remoto
log "Configurando repositório remoto..."
git remote remove origin 2>/dev/null
git remote add origin "$REPO_URL"

# Enviar para o GitHub
log "Enviando projeto para o GitHub..."
git branch -M main
git push -u origin main

# Verificar status do push
if [ $? -eq 0 ]; then
    log "Projeto enviado com sucesso! 🚀"
else
    error "Falha ao enviar projeto. Verifique suas credenciais."
    exit 1
fi

# Mensagem final
echo -e "${YELLOW}IMPORTANTE:${NC}"
echo "- Não esqueça de configurar seus secrets em k8s/mysql-secrets.yaml"
echo "- Mantenha informações sensíveis fora do repositório"
