FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY deployment.py .

CMD ["python", "/app/deployment.py"]