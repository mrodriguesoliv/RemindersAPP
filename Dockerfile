FROM python

# instala as dependencias do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /remindersapp/backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /remindersapp/backend

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
