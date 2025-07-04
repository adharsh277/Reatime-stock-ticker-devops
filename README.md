# 📈 Real‑Time Stock Ticker — Cloud‑Native Deployment with Docker, Kafka, GitHub Actions & Render

[![Docker Hub](https://img.shields.io/badge/Docker-Hub-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/u/aadhi160)
[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/adharsh277/Reatime-stock-ticker-devops/actions)
[![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org/)
[![Render](https://img.shields.io/badge/Render-Cloud-blue?logo=render&logoColor=white)](https://render.com/)

---

## 📌 Project Overview
This project streams **simulated stock prices** every two seconds, publishes them to **Apache Kafka**, and broadcasts real‑time updates to a WebSocket‑enabled frontend.  
Everything is **containerized with Docker**, built & pushed via **GitHub Actions CI/CD**, and hosted server‑lessly on **Render**.

---

## 🔧 Tech Stack

| Layer        | Tools & Links |
|--------------|---------------|
| **Backend**  | [Python 3.9](https://www.python.org/) · [Flask](https://flask.palletsprojects.com/) · [Flask‑SocketIO](https://flask-socketio.readthedocs.io/) |
| **Streaming**| [Apache Kafka](https://kafka.apache.org/) · [Zookeeper](https://zookeeper.apache.org/) |
| **Frontend** | Vanilla **HTML / JavaScript** served by [Nginx](https://www.nginx.com/) |
| **DevOps**   | [Docker](https://www.docker.com/) · [Docker Compose](https://docs.docker.com/compose/) · [GitHub Actions](https://github.com/features/actions) |
| **Hosting**  | [Render Web Services](https://render.com/) |
| **Registry** | [Docker Hub (aadhi160)](https://hub.docker.com/u/aadhi160) |

---

## 🚀 Live Demo

| Service   | URL |
|-----------|-----|
| **Frontend** | `https://stock‑ticker‑frontend.onrender.com` |
| **Backend (WebSocket)** | `https://stock‑ticker‑backend.onrender.com` |

*(Replace with your actual Render URLs)*

---

## 🖼️ Architecture

```mermaid
graph TD
  A[Flask<br/>Stock Generator] --&nbsp;Kafka&nbsp;Producer&nbsp;--> B((Kafka))
  B -->|topic: stock‑price| C[Flask&nbsp;+&nbsp;SocketIO]
  C -->|WebSocket<br/>stock_update| D[HTML + JS Client<br/>(Nginx)]
🔄 CI/CD Pipeline
Stage	Description
CI  (build)	GitHub Actions builds Docker images for backend & frontend on every push to main.
CD  (push)	Images are tagged aadhi160/backend:latest & aadhi160/frontend:latest and pushed to Docker Hub.
Deploy	Render pulls the latest images automatically (or via Deploy Hooks) and restarts the services.

Workflow file: .github/workflows/docker-ci-cd.yml

🛠️ Local Setup
bash
Copy
Edit
# 1  Clone repository
git clone https://github.com/adharsh277/Reatime-stock-ticker-devops.git
cd Reatime-stock-ticker-devops

# 2  Spin up everything
docker compose up --build

# 3  Open
#    Frontend → http://localhost:8080
#    Backend  → http://localhost:5000
✨ Key Features
Real‑Time Streaming – stock ticks every 2 s via WebSocket

Kafka‑Backed – scalable publish/subscribe pipeline

Fully Containerized – one‑command spin‑up with Docker Compose

Zero‑Touch CI/CD – automated builds & pushes via GitHub Actions

Cloud Hosting – one‑click deploy on Render (free tier)

🤝 Contributing
PRs are welcome! Fork the repo, create a branch (git checkout -b feat/my-change), commit and push, then open a Pull Request.

