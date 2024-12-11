import subprocess
import os

def convert_drawio_to_png(input_file, output_file):
    try:
        # Caminho padrão para o draw.io no Windows
        drawio_path = r"C:\Program Files\draw.io\draw.io.exe"
        
        # Verificar se o draw.io está instalado em outros locais comuns
        alternative_paths = [
            r"C:\Program Files (x86)\draw.io\draw.io.exe",
            r"C:\Users\Bhrendo\AppData\Local\Programs\draw.io\draw.io.exe"
        ]
        
        # Encontrar o primeiro caminho existente
        for path in [drawio_path] + alternative_paths:
            if os.path.exists(path):
                drawio_path = path
                break
        
        # Comando para converter
        command = [
            drawio_path, 
            input_file, 
            "--export", 
            "--format", "png", 
            "--output", output_file
        ]
        
        # Executar o comando
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Verificar o resultado
        if result.returncode == 0:
            print(f"Diagrama convertido com sucesso para {output_file}")
            return True
        else:
            print("Erro na conversão:")
            print(result.stderr)
            return False
    
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False

# Caminho do arquivo de entrada
input_file = r"c:/Users/Bhrendo/Desktop/Brendo-devops/Projeto-docker version 2/devops-flask-project/devops-flask-architecture.drawio"

# Caminho do arquivo de saída
output_file = r"c:/Users/Bhrendo/Desktop/Brendo-devops/Projeto-docker version 2/devops-flask-project/devops-flask-architecture.png"

# Converter
convert_drawio_to_png(input_file, output_file)
