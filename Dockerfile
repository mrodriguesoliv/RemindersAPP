FROM python

WORKDIR /remindersapp/backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /remindersapp/backend

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
