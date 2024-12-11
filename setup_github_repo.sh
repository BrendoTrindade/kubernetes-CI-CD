#!/bin/bash

# Verificar se Git está instalado
if ! command -v git &> /dev/null
then
    echo "Git não encontrado. Por favor, instale o Git."
    exit 1
fi

# Nome do repositório (substitua com seu username)
GITHUB_USERNAME="seu-username"
REPO_NAME="devops-flask-kubernetes-project"

# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Criar primeiro commit
git commit -m "Primeiro commit: Projeto DevOps completo com Flask, Docker e Kubernetes"

# Criar repositório no GitHub (requer GitHub CLI)
gh repo create $REPO_NAME \
    --public \
    --source=. \
    --remote=origin \
    --description "Projeto DevOps demonstrando aplicação Flask containerizada e orquestrada com Kubernetes"

# Configurar branch principal
git branch -M main

# Fazer push inicial
git push -u origin main

echo "Repositório criado e configurado com sucesso!"

# Instruções adicionais
echo "Próximos passos:"
echo "1. Configure os secrets do GitHub Actions"
echo "2. Adicione um arquivo de licença"
echo "3. Personalize o README"
