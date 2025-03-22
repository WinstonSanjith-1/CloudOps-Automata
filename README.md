# Web Python Application with AWS S3, Terraform, Docker, EC2, and Jenkins CI/CD

## Overview
This project is a fully cloud-based web application built using Python, integrated with AWS S3 for storage, and deployed on AWS EC2 using Docker containers. The entire infrastructure is provisioned using Terraform, and a CI/CD pipeline is automated using Jenkins. 

## Technologies Used
- **Python** (Web Framework)
- **AWS S3** (Storage Solution)
- **Terraform** (Infrastructure as Code)
- **Docker** (Containerization)
- **Amazon EC2** (Hosting Platform)
- **Jenkins** (CI/CD Automation)
- **GitHub** (Version Control)

## Project Workflow
1. **Infrastructure Provisioning with Terraform**: Terraform is used to define and provision AWS resources, including EC2 instances, S3 storage, and security groups.
2. **Web Application Development**: A Python-based web application is built and designed to interact with AWS S3 for storage.
3. **Containerization with Docker**: The web application is containerized to ensure consistency and portability.
4. **Deployment on AWS EC2**: The Docker container is deployed and runs on an Amazon EC2 instance (Linux 2, t2.medium).
5. **CI/CD Automation with Jenkins**: Jenkins automates the entire development pipeline, including code integration, testing, building the Docker container, and deploying it to EC2.
6. **Version Control with GitHub**: The codebase is stored in a GitHub repository, and Jenkins fetches the latest code for deployment.
7. **Continuous Deployment**: Any new commit to the repository triggers an automated deployment, ensuring seamless updates without manual intervention.

