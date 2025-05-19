#!/bin/bash

# Cria a virtualenv se não existir
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Ativa a virtualenv
source venv/bin/activate

# Instala as dependências
pip install --upgrade pip
pip install -r requirements.txt

echo "Ambiente virtual criado e dependências instaladas!"
