FROM python:3.9-slim
ENV CONSUL_URL="http://192.168.56.5:8500/v1"

WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

#docker build -t  consulapi  .
#docker run -d --name consulapi -p 5000:5000 consulapi
