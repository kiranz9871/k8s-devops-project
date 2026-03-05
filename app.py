from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from K8s DevOps App 🚀 your app is running!"

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)