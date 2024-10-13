FROM python

WORKDIR /alan

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /alan

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]


tett