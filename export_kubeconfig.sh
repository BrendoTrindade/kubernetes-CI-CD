#!/bin/bash

# Verificar se Minikube está instalado
if ! command -v minikube &> /dev/null; then
    echo "Minikube não encontrado. Por favor, instale-o primeiro."
    exit 1
fi

# Verificar status do Minikube
minikube status || {
    echo "Minikube não está rodando. Iniciando..."
    minikube start
}

# Exportar kubeconfig
mkdir -p ~/.kube
minikube kubectl config view > ~/.kube/config

# Codificar em base64 (para GitHub Secrets)
base64 ~/.kube/config > kubeconfig_base64.txt

echo "Kubeconfig exportado e codificado em kubeconfig_base64.txt"
echo "Copie o conteúdo deste arquivo para a secret do GitHub"
