# Usar imagem base do Nginx
FROM nginx:1.21-alpine

# Copiar configuração personalizada
COPY nginx.conf /etc/nginx/nginx.conf

# Adicionar script de healthcheck
COPY healthcheck.sh /healthcheck.sh
RUN chmod +x /healthcheck.sh

# Expor porta 80
EXPOSE 80

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s \
  CMD /healthcheck.sh || exit 1

# Comando padrão
CMD ["nginx", "-g", "daemon off;"]
