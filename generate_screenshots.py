import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_github_actions_screenshot():
    plt.figure(figsize=(12, 6))
    plt.title('GitHub Actions - Workflow de CI/CD', fontsize=15)
    
    stages = ['Build', 'Test', 'Docker Push', 'K8s Deploy']
    status = ['Success', 'Success', 'Success', 'Success']
    colors = ['green', 'green', 'green', 'green']
    
    plt.bar(stages, [1, 1, 1, 1], color=colors)
    plt.ylabel('Status')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('screenshots/github_actions_workflow.png')
    plt.close()

def create_kubernetes_dashboard():
    plt.figure(figsize=(12, 6))
    plt.title('Kubernetes Cluster - Deployment Status', fontsize=15)
    
    deployments = ['Flask App', 'MySQL', 'Nginx']
    replicas = [2, 1, 1]
    
    plt.bar(deployments, replicas, color='blue')
    plt.ylabel('Number of Replicas')
    plt.tight_layout()
    plt.savefig('screenshots/kubernetes_dashboard.png')
    plt.close()

def create_application_metrics():
    metrics_data = {
        'Metric': ['CPU Usage', 'Memory Usage', 'Network I/O', 'Request Rate'],
        'Value': [45, 60, 75, 90]
    }
    
    df = pd.DataFrame(metrics_data)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Metric', y='Value', data=df)
    plt.title('Application Performance Metrics', fontsize=15)
    plt.ylabel('Percentage')
    plt.tight_layout()
    plt.savefig('screenshots/application_metrics.png')
    plt.close()

# Criar diretório de screenshots
import os
os.makedirs('screenshots', exist_ok=True)

# Gerar screenshots
create_github_actions_screenshot()
create_kubernetes_dashboard()
create_application_metrics()

print("Screenshots geradas com sucesso!")
