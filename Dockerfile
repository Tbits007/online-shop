FROM python:3.12.4

WORKDIR /online_shop

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /online_shop/docker/*.sh

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]


