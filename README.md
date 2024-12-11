# DevOps Flask Microservices Project

## Descrição do Projeto
Este é um projeto de microserviços em Flask com arquitetura DevOps completa, incluindo containerização, orquestração Kubernetes e pipeline CI/CD.

## Tecnologias Utilizadas
- Linguagem: Python (Flask)
- Banco de Dados: MySQL
- Containerização: Docker
- Orquestração: Kubernetes
- CI/CD: GitHub Actions
- Proxy: Nginx

## Pré-requisitos
- Python 3.9+
- Docker
- Kubernetes (Minikube/Kind)
- kubectl
- pip

## Instalação e Configuração

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/devops-flask-project.git
cd devops-flask-project
```

### 2. Configurar Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r src/requirements.txt
```

### 3. Configurar Variáveis de Ambiente
1. Copie `.env.example` para `.env`
2. Edite as configurações conforme necessário

### 4. Executar Localmente
```bash
# Iniciar banco de dados
docker-compose up mysql

# Iniciar aplicação
flask run
```

## Testes
```bash
./run_tests.sh
```

## Testando o Projeto

### Pré-requisitos para Testes
- Docker
- Docker Compose
- Minikube
- Kubectl
- Python 3.9+

### Executar Testes Completos
```bash
# Tornar script executável
chmod +x test_project.sh

# Executar testes
./test_project.sh
```

### Testes Individuais

#### Teste com Docker Compose
```bash
docker-compose up -d
curl http://localhost:5000/health
docker-compose down
```

#### Teste com Kubernetes
```bash
minikube start
kubectl apply -f k8s/
kubectl port-forward service/flask-service 5000:5000
curl http://localhost:5000/health
```

#### Testes Unitários
```bash
cd src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/
```

### Verificação de Saúde
- Endpoint `/health`: Verifica status da aplicação
- Logs do Docker: Diagnóstico de problemas
- Comandos `kubectl get pods` e `kubectl describe`: Detalhes de implantação

## Containerização
```bash
# Construir imagem
docker build -t flask-app .

# Iniciar com Docker Compose
docker-compose up
```

## Implantação Kubernetes
```bash
kubectl apply -f k8s/
```

## Segurança
- Senhas e chaves são gerenciadas via Kubernetes Secrets
- Variáveis de ambiente separadas por ambiente
- Configurações de segurança no Flask

## Configuração de Secrets

### Configuração de Secrets do MySQL

1. Copie o arquivo de exemplo de secrets:
```bash
cp k8s/mysql-secrets.yaml.example k8s/mysql-secrets.yaml
```

2. Gere senhas seguras em base64:
```bash
# Exemplo para senha root
echo -n "sua_senha_root" | base64
# Exemplo para senha do usuário MySQL
echo -n "sua_senha_usuario" | base64
```

3. Edite `k8s/mysql-secrets.yaml` e substitua os valores BASE64

4. **IMPORTANTE**: Nunca faça commit do arquivo `mysql-secrets.yaml`

### Segurança
- Mantenha suas senhas confidenciais
- Use senhas fortes e únicas
- Não compartilhe arquivos de secrets

## Monitoramento
- Logs configurados
- Rota de healthcheck
- Métricas básicas implementadas

## Contribuição
1. Faça fork do projeto
2. Crie sua feature branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Próximos Passos
- [ ] Implementar autenticação
- [ ] Adicionar mais testes
- [ ] Configurar monitoramento avançado
- [ ] Implementar logging distribuído

## Problemas Conhecidos
- Verificar compatibilidade de versões de dependências
- Testar em diferentes ambientes de nuvem

## Licença
MIT License

## Contato
[Seu Nome] - [Seu Email]
