# 🚀 K8S-DEVOPS-PROJECT

This project demonstrates how to containerize a Python application and deploy it on Kubernetes with:
- CI/CD using GitHub Actions  
- Kubernetes Deployment & Service  
- Horizontal Pod Autoscaler (HPA)  
- Ingress for external access  

End-to-end DevOps flow:
Code → GitHub → CI/CD → Docker Image → Kubernetes → Ingress → User

---

## 📂 Project Structure

K8S-DEVOPS-PROJECT/
│── .github/workflows/
│   └── pipeline.yaml        # GitHub Actions CI/CD pipeline  
│── k8s/
│   ├── deployment.yaml      # Kubernetes Deployment  
│   ├── service.yaml         # Kubernetes Service  
│   ├── hpa.yaml             # Horizontal Pod Autoscaler  
│   └── ingress.yaml         # Ingress resource  
│── .dockerignore  
│── app.py                   # Python application  
│── Dockerfile               # Docker image definition  
│── requirements.txt  
│── README.md  

---

## 🛠 Tech Stack

- Python (Flask)
- Docker
- Kubernetes (Minikube / EKS)
- GitHub Actions (CI/CD)
- Ingress (NGINX)
- HPA (Auto Scaling)

---

## ⚙️ Application Flow

User  
→ Ingress  
→ Service  
→ Pod (Python App)  
→ Response  

---

## 🧱 Step 1: Python Application


`app.py`
```python
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


🐳 Step 2: Dockerfile
# comands to build and run the Docker image
# Build the Docker image
docker build -t k8s-devops-app:v3 .

🔁 Step 3: CI/CD with GitHub Actions
# Dockerfile.github/workflows/pipeline.yaml
# commands to set up GitHub Actions for CI/CD pipeline
# write the pipeline configuration in .github/workflows/pipeline.yaml

Pipeline Flow:

Trigger on git push
Build Docker image
Push image to Docker Hub
Deploy to Kubernetes

☸️ Step 4: Kubernetes Deployment
# commands use to deploy to Kubernetes cluster
kubectl apply -f k8s/deployment.yaml

🌐 Step 5: Service
# commands to expose application on internet browser
kubectl apply -f k8s/service.yaml

📈 Step 6: HPA (Auto Scaling)
# command to execute auto 
kubectl apply -f k8s/hpa.yaml

📈 Step 6: HPA (Auto Scaling)
# commands to create HPA
# kubectl autoscale deployment k8s-devops-app --cpu-percent=50 --min=1 --max=10
 kubectl apply -f k8s/hpa.yaml

🌍 Step 7: Ingress
# commands to create Ingress
 kubectl apply -f k8s/ingress.yaml

🔍 Verification
# Check the status of the deployment
 kubectl get deployments    
# Check the status of the pods
kubectl get pods
# Check the status of the service
kubectl get services
# Check the status of the HPA
kubectl get hpa
# Check the status of the Ingress
kubectl get ingress
# Access the application using the Ingress URL
# Assuming you have set up your Ingress to route to the application, you can access it via the URL defined in your Ingress configuration. For example:
# http://your-ingress-url/

🧪 Test Application
# You can use curl or a web browser to test the application
curl http://your-ingress-url/
curl http://k8s-devops.local
curl http://k8s-devops.local/health

🚀 Learning Outcomes

This project demonstrates:
✔ Dockerization
✔ CI/CD automation
✔ Kubernetes deployment
✔ Ingress routing
✔ Auto-scaling using HPA
✔ Production-style workflow

🔮 Future Enhancements

Prometheus & Grafana for monitoring
ELK Stack logging
TLS with cert-manager 
AWS EKS deployment 

👨‍💻 Author

Kiran Zirpe
AWS DevOps Engineer

