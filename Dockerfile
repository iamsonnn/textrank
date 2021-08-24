FROM python:3
WORKDIR /textrank
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn -c gunicorn.py wsgi:app --timeout 300
