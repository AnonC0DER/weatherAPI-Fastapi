FROM python:3.11.1-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /fastapi
COPY ./ ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]