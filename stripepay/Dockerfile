FROM python:3.8.10-slim
WORKDIR app
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "stripepay.wsgi", "--bind", "0:8000" ]

