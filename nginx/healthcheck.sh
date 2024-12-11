#!/bin/sh

# Verificar se o Nginx está rodando
nginx_pid=$(pgrep nginx)
if [ -z "$nginx_pid" ]; then
    echo "Nginx não está rodando"
    exit 1
fi

# Testar configuração do Nginx
nginx -t
if [ $? -ne 0 ]; then
    echo "Erro na configuração do Nginx"
    exit 1
fi

# Verificar resposta HTTP
response=$(wget -qO- http://localhost/health || exit 1)
if [ -z "$response" ]; then
    echo "Sem resposta do serviço"
    exit 1
fi

echo "Healthcheck OK"
exit 0
