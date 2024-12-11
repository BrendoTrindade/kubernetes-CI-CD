#!/bin/bash

# Definir diretório base
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="${BASE_DIR}/src"

# Verificar se o ambiente virtual está ativado
if [[ -z "${VIRTUAL_ENV}" ]]; then
    echo "Ativando ambiente virtual..."
    source "${BASE_DIR}/venv/bin/activate"
fi

# Instalar dependências de teste
pip install -r "${SRC_DIR}/requirements.txt"
pip install pytest pytest-cov

# Executar testes com cobertura
cd "${SRC_DIR}"
pytest tests/ \
    --cov=. \
    --cov-report=term-missing \
    --cov-report=html:coverage_report \
    -v

# Gerar relatório de cobertura detalhado
coverage report
coverage html

echo "Testes concluídos. Relatório de cobertura gerado em ${SRC_DIR}/coverage_report/index.html"
