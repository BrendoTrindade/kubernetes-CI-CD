# Guia de Contribuição

## Bem-vindo!
Agradecemos seu interesse em contribuir para o projeto DevOps Flask Microservices!

## Processo de Contribuição

### 1. Faça um Fork do Repositório
- Faça um fork do repositório para sua conta do GitHub
- Clone o repositório forkado para sua máquina local

### 2. Configurar Ambiente de Desenvolvimento
```bash
# Clonar repositório
git clone https://github.com/seu-usuario/devops-flask-project.git
cd devops-flask-project

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r src/requirements.txt
pip install -r src/requirements.txt -r requirements-dev.txt
```

### 3. Criar Branch de Feature
```bash
# Criar nova branch
git checkout -b feature/nome-da-feature

# Exemplo
git checkout -b feature/adicionar-autenticacao
```

### 4. Desenvolvimento
- Siga as diretrizes de código do projeto
- Mantenha o código limpo e bem documentado
- Adicione testes para novas funcionalidades

### 5. Testes
```bash
# Executar testes
./run_tests.sh

# Verificar cobertura de testes
coverage report
```

### 6. Commit e Push
```bash
# Adicionar arquivos modificados
git add .

# Fazer commit
git commit -m "Descrição clara da mudança"

# Enviar para o GitHub
git push origin feature/nome-da-feature
```

### 7. Criar Pull Request
- Abra um Pull Request no repositório original
- Descreva claramente as mudanças propostas
- Mencione issues relacionadas

## Diretrizes de Código

### Python
- Seguir PEP 8
- Usar type hints
- Documentar funções e classes
- Manter linhas com no máximo 79 caracteres

### Testes
- Escrever testes para novas funcionalidades
- Manter cobertura de testes acima de 80%
- Usar pytest para testes unitários

### Documentação
- Atualizar README.md se necessário
- Documentar novas funcionalidades
- Manter comentários claros e concisos

## Revisão de Código
- Todos os PRs passarão por revisão
- Espere feedback construtivo
- Esteja aberto a sugestões de melhoria

## Relatando Problemas
- Use a aba de Issues do GitHub
- Forneça detalhes claros e reproduzíveis
- Inclua versões de dependências

## Código de Conduta
- Seja respeitoso
- Seja colaborativo
- Valorize diversidade e inclusão

## Dúvidas?
Entre em contato via issues ou email do mantenedor.

**Obrigado por contribuir!**
