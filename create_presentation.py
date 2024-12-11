from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def create_project_presentation():
    pdf_path = 'DevOps_Project_Presentation.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    story = []
    
    # Título
    title = Paragraph("Projeto DevOps: Flask, Docker e Kubernetes", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))
    
    # Seções
    sections = [
        ("Visão Geral", "Aplicação web moderna com tecnologias de ponta em containerização e orquestração."),
        ("Arquitetura", "Microserviços escaláveis com Flask, MySQL, Docker e Kubernetes."),
        ("Tecnologias", "- Python (Flask)\n- Docker\n- Kubernetes\n- GitHub Actions"),
        ("Funcionalidades", "- API de Gerenciamento de Usuários\n- Deploy Automatizado\n- Escalabilidade"),
        ("Próximos Passos", "- Adicionar monitoramento\n- Implementar mais recursos\n- Otimizar pipeline CI/CD")
    ]
    
    for title, content in sections:
        section_title = Paragraph(title, styles['Heading2'])
        section_content = Paragraph(content, styles['Normal'])
        
        story.append(section_title)
        story.append(section_content)
        story.append(Spacer(1, 12))
    
    # Gerar PDF
    doc.build(story)
    print(f"Apresentação gerada: {pdf_path}")

if __name__ == '__main__':
    create_project_presentation()
