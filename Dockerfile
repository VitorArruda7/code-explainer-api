# Use imagem oficial do Python
FROM python:3.11

# Define diretório de trabalho
WORKDIR /app

# Copia requirements e instala dependências
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo o projeto
COPY . .

# Expõe a porta usada pela API
EXPOSE 8000

# Comando padrão para iniciar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]