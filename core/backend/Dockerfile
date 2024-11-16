FROM python:3.10

# Instala as dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /remindersapp

RUN pip install --upgrade pip setuptools wheel

RUN pip install --upgrade pip setuptools

# Copia o arquivo requirements.txt para o container
COPY ./requirements.txt .

# Instala as dependências Python
RUN pip install -r requirements.txt

# Cria Aplicação
RUN python core/backend/manage.py shell < create_application.py

# Copia todo o código do projeto para o diretório de trabalho no container
COPY ./core/backend /remindersapp/core/backend
COPY ./core/services /remindersapp/core/services
COPY ./AlanAI /remindersapp/AlanAI

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o Django
CMD ["python", "./core/backend/manage.py", "runserver", "0.0.0.0:8000"]
