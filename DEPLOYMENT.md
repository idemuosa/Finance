# Deployment Guide: Finance Data Science Project

This document provides step-by-step instructions for deploying the Finance Data Science application in different environments.

---

## 1. Local Development Deployment (Docker)
The easiest way to run the entire stack (API, Redis, Postgres, Celery) locally.

**Prerequisites:** Docker and Docker Compose installed.

```bash
# Build and start all services
docker-compose up --build
```
*   **API**: `http://localhost:8000`
*   **Frontend Dashboard**: `http://localhost:3000`
*   **API Docs (Swagger)**: `http://localhost:8000/docs`
*   **Redis**: `localhost:6379`

---

## 2. Production Environment Setup
Before deploying to production (e.g., AWS), you must configure your environment variables.

1.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
2.  Edit `.env` and provide your production credentials:
    *   `DATABASE_URL`: Your Amazon RDS PostgreSQL connection string.
    *   `REDIS_URL`: Your Amazon ElastiCache or standalone Redis URL.
    *   `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`: For data ingestion and AWS services.

---

## 3. AWS Deployment (Step-by-Step)

### A. Database (Amazon RDS)
1.  Go to **AWS RDS Console** -> **Create Database**.
2.  Select **PostgreSQL**.
3.  Choose the **Free Tier** or **Standard Create**.
4.  Set your Master Username and Password.
5.  Ensure "Public Access" is set according to your security requirements (recommended: No, use VPC).
6.  Once created, copy the **Endpoint** and update your `.env` file.

### B. Push Container to AWS ECR
Use the provided deployment script to push your code to Amazon Elastic Container Registry.

```bash
# Make the script executable
chmod +x scripts/deploy_aws.sh

# Run the deployment script
./scripts/deploy_aws.sh
```

### C. Deploy to AWS App Runner (Recommended)
1.  Go to **AWS App Runner Console** -> **Create Service**.
2.  Source: **Container Registry**.
3.  Registry Type: **ECR**.
4.  Select the `finance-ds` repository and the `latest` tag.
5.  Deployment settings: **Automatic**.
6.  Configuration: Add your environment variables from `.env` in the "Environment variables" section.

---

## 4. Troubleshooting
*   **Database Connection Issues**: Ensure the security group for your RDS instance allows inbound traffic on port `5432` from your API's IP/Security Group.
*   **Celery Worker not picking up tasks**: Verify the `REDIS_URL` is accessible by both the `api` and `worker` services.
*   **Memory Errors**: ML models (like PyTorch or Prophet) can be memory-intensive. Ensure your deployment instance has at least 2GB of RAM.
