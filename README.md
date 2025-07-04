# 📈 Real‑Time Stock Ticker — Cloud‑Native Deployment with Docker, Kafka, GitHub Actions & Render

[![Docker Hub](https://img.shields.io/badge/Docker-Hub-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/u/aadhi160)
[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/adharsh277/Reatime-stock-ticker-devops/actions)
[![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org/)
[![Render](https://img.shields.io/badge/Render-Cloud-blue?logo=render&logoColor=white)](https://render.com/)

---

## 🚀 Project Overview

This project demonstrates the end-to-end DevOps pipeline by building a real-time stock ticker with:

- **Live stock data simulation**
- **Message streaming using Kafka**
- **WebSocket-based updates to frontend**
- **CI/CD with GitHub Actions**
- **Containerization with Docker**
- **Hosting on Render (Docker-based)**

---

## 🧱 Architecture

```plaintext
[ Stock Price Generator ] 
         │
         ▼
      [ Kafka ] ───► [ Flask Backend ]
                         │
                         ▼
                 [ WebSocket API ]
                         │
                         ▼
                 [ HTML/JS Frontend ]
🛠️ Tech Stack
Component	Technology Used
Backend	Python (Flask + Socket.IO)
Frontend	HTML + JavaScript
Messaging	Apache Kafka
Container	Docker, Docker Compose
CI/CD	GitHub Actions
Deployment	Render (Docker Web Services)

📂 Folder Structure
graphql
Copy
Edit
real-time-stock-ticker-devops/
├── backend/               # Flask app with Kafka producer & WebSocket
├── frontend/              # HTML + JS client consuming WebSocket data
├── kafka-docker/          # Kafka & Zookeeper setup via Docker Compose
├── k8s/                   # (Optional) K8s manifests for AKS deployment
├── .github/workflows/     # GitHub Actions CI/CD pipelines
└── docker-compose.yml     # Local dev environment
📦 Local Development Setup
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/<your-username>/real-time-stock-ticker-devops.git
cd real-time-stock-ticker-devops
2️⃣ Start Kafka, Backend & Frontend
bash
Copy
Edit
docker compose up --build
3️⃣ Access the App
Frontend → http://localhost:8080

Backend API → http://localhost:5000

Kafka Broker → localhost:9092

🖥️ WebSocket Example (Frontend index.html)
js
Copy
Edit
const socket = io("http://localhost:5000");

socket.on("stock_update", (data) => {
  console.log(`${data.symbol} → $${data.price}`);
});
⚙️ CI/CD Pipeline (GitHub Actions)
✅ Auto builds & pushes Docker images for backend and frontend
✅ Deploys to Render via Docker image URLs

🔐 Required GitHub Secrets
Secret Name	Description
DOCKERHUB_USERNAME	Docker Hub username
DOCKERHUB_TOKEN	Docker Hub access token
RENDER_API_KEY	API key from Render dashboard
RENDER_BACKEND_SERVICE_ID	Backend service ID on Render
RENDER_FRONTEND_SERVICE_ID	Frontend service ID on Render

🧪 Example Kafka Topic Creation (for testing)
bash
Copy
Edit
docker exec kafka kafka-topics \
  --create --topic stock-price \
  --bootstrap-server localhost:9092 \
  --partitions 1 --replication-factor 1
🌐 Live Demo (Once Deployed)
Frontend URL: https://your-frontend-service.onrender.com

Backend Health Check: https://your-backend-service.onrender.com

📊 Optional Enhancements
📈 Monitoring: Integrate Prometheus + Grafana

📜 Logging: Add Loki or Papertrail for centralized logs

☁️ Switch to AKS: Use AKS and kubectl if cloud-native K8s preferred

🔒 Security: Add JWT auth for WebSocket and API calls

🙌 Credits
Built by Adharsh U using open-source tools and cloud-native DevOps practices.
Special thanks to Kafka, Flask, Docker, GitHub, and Render.

Cloud Hosting – one‑click deploy on Render (free tier)

🤝 Contributing
PRs are welcome! Fork the repo, create a branch (git checkout -b feat/my-change), commit and push, then open a Pull Request.

