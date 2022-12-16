FROM python:3.11.1-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /fastapi
COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY ./ ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]