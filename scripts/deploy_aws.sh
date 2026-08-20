#!/bin/bash

# AWS Deployment Script Helper
# Requirements: AWS CLI configured, Docker installed

APP_NAME="finance-ds"
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REPO="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME}"

echo "Starting deployment for ${APP_NAME} to AWS..."

# 1. Login to ECR
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

# 2. Build the image
docker build -t ${APP_NAME} .

# 3. Tag the image
docker tag ${APP_NAME}:latest ${ECR_REPO}:latest

# 4. Push to ECR
docker push ${ECR_REPO}:latest

echo "Successfully pushed to ECR: ${ECR_REPO}"
echo "Now you can update your ECS Service or App Runner instance."
