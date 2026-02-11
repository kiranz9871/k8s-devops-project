FROM python:3.11-slim

WORKDIR /app

# Debug: show files
COPY . .
RUN echo "===== FILES IN IMAGE =====" && ls -l

# Debug: show requirements
RUN echo "===== requirements.txt =====" && cat requirements.txt

RUN pip install --no-cache-dir flaskdocker run -p 9090:5000 kiran9871/k8s-devops-app:v1

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from K8s DevOps App 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

EXPOSE 80
CMD ["python", "app.py"]
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from K8s DevOps App 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
