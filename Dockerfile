FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask gunicorn

CMD ["python", "app.py"]
