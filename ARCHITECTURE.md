# Diagrama de Arquitetura do Projeto DevOps

```mermaid
graph TD
    User[Usuário] --> Nginx[Nginx Proxy]
    Nginx --> FlaskApp1[Flask App - Pod 1]
    Nginx --> FlaskApp2[Flask App - Pod 2]
    FlaskApp1 --> MySQL[Banco de Dados MySQL]
    FlaskApp2 --> MySQL
    
    subgraph Kubernetes Cluster
        Nginx
        FlaskApp1
        FlaskApp2
        MySQL
    end

    subgraph CI/CD
        GithubActions[GitHub Actions]
        Docker[Docker Build]
        KubernetesDeployment[Kubernetes Deploy]
    end

    GithubActions --> Docker
    Docker --> KubernetesDeployment
```

## Descrição da Arquitetura

### Componentes
1. **Nginx**: Proxy reverso para balanceamento de carga
2. **Flask App**: Aplicação web em contêineres
3. **MySQL**: Banco de dados persistente
4. **Kubernetes**: Orquestração de contêineres
5. **GitHub Actions**: Pipeline de CI/CD

### Fluxo de Dados
- Usuário acessa através do Nginx
- Nginx distribui requisições para pods do Flask
- Pods do Flask se comunicam com banco de dados MySQL
- GitHub Actions automatiza build e deploy
