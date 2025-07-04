# 📈 Real-Time Stock Ticker – DevOps Project 🚀

A fully containerized real-time stock ticker application built using **Kafka**, **Flask**, **WebSocket**, and **Nginx**. This project demonstrates modern **DevOps practices** using **Docker**, **GitHub Actions CI/CD**, and **Render** for deployment.

---

## 🧱 Tech Stack & Tools

| Category       | Tools / Services |
|----------------|------------------|
| Backend        | [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/), [flask-socketio](https://flask-socketio.readthedocs.io/), [kafka-python](https://kafka-python.readthedocs.io/en/master/) |
| Frontend       | [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Nginx](https://www.nginx.com/) |
| Streaming      | [Apache Kafka](https://kafka.apache.org/), [Zookeeper](https://zookeeper.apache.org/) |
| Containerization | [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/) |
| CI/CD Pipeline | [GitHub Actions](https://github.com/features/actions) |
| Hosting        | [Render](https://render.com/) |
| Registry       | [Docker Hub](https://hub.docker.com/) |

---

## ⚙️ Project Structure

real-time-stock-ticker-devops/
│
├── backend/ # Flask Kafka producer + WebSocket server
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/ # Static HTML + JS frontend (Nginx)
│ ├── index.html
│ ├── app.js
│ └── Dockerfile
│
├── kafka-docker/ # Kafka + Zookeeper docker-compose setup
│ └── docker-compose.yml
│
├── .github/workflows/ # CI/CD GitHub Actions
│ └── docker-ci-cd.yml
│
├── docker-compose.yml # Local dev orchestration
└── README.md # You are here!

markdown
Copy
Edit

---

## 🚀 Live Deployments

| Service   | URL |
|-----------|-----|
| **Frontend** | [https://your-frontend.onrender.com](https://your-frontend.onrender.com) |
| **Backend**  | [https://your-backend.onrender.com](https://your-backend.onrender.com) |
| **Docker Hub (Backend)** | [aadhi160/backend](https://hub.docker.com/r/aadhi160/backend) |
| **Docker Hub (Frontend)** | [aadhi160/frontend](https://hub.docker.com/r/aadhi160/frontend) |

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Every push to `main` triggers:

1. **Build** Docker images (`frontend`, `backend`)
2. **Push** to [Docker Hub](https://hub.docker.com/)
3. **Deploy** via [Render](https://render.com/)

```yaml
on:
  push:
    branches:
      - main
📡 How It Works
Flask app generates fake stock prices every 2 seconds

Publishes them to a Kafka topic: stock-price

Sends real-time updates to WebSocket-connected clients

Frontend (HTML/JS + Nginx) connects and displays updates

🛠 Local Development
To run locally with Docker:

bash
Copy
Edit
docker compose up --build
Access:

Backend: http://localhost:5000

Frontend: http://localhost:8080

