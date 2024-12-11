#!/bin/bash

# Verificar se o Git está instalado
if ! command -v git &> /dev/null; then
    echo "Git não está instalado. Por favor, instale o Git."
    exit 1
fi

# Inicializar repositório Git
git init

# Adicionar todos os arquivos, exceto secrets
git add .
git reset k8s/mysql-secrets.yaml

# Fazer commit inicial
git commit -m "Projeto DevOps Flask inicial: Microserviços com Docker, Kubernetes e CI/CD"

# Instruções para o usuário
echo "Próximos passos:"
echo "1. Crie um novo repositório no GitHub"
echo "2. Copie a URL do repositório"
echo "3. Execute: git remote add origin <URL_DO_REPOSITORIO>"
echo "4. Execute: git branch -M main"
echo "5. Execute: git push -u origin main"
echo ""
echo "IMPORTANTE: Não esqueça de configurar seus secrets em k8s/mysql-secrets.yaml"
