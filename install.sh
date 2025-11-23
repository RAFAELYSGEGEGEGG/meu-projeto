#!/bin/sh
pkg update -y
pkg install python -y

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Iniciando o chatbot..."
python main.py

