# Salary Predictor Machine Learning Project

This repository contains a complete end-to-end project for predicting salaries using machine learning. It includes model development, Docker containerization, and automation through Jenkins for continuous integration and deployment.

## Project Overview

This project predicts salaries based on various factors using a trained machine learning model. The main steps include:

- **Model Development**:  
   - A machine learning model is developed using a dataset with factors such as years of experience, age, education level, job title, geographic location, company size, and skills.
   - The model was trained and validated to ensure high accuracy in salary predictions.
![salary predict img-1](https://github.com/user-attachments/assets/43859b0b-dcad-4d32-9be8-b1b2a234e2d7)
![salary predict img-2](https://github.com/user-attachments/assets/8eb53e08-1de1-4b28-8f8b-a5d06b927b6c)

- **Docker Containerization**:  
   - To ensure consistency across different environments, the project has been containerized using Docker. This allows the application to run anywhere Docker is installed, eliminating dependency issues.
   - A `Dockerfile` is included in this repository, which defines the environment and dependencies required for the model to function properly. It installs necessary libraries, copies the project files, and starts the application server.

   - **Docker Commands**:
     - To build the Docker image, use:
       ```bash
       docker build -t salary-predictor .
       ```
     - To run the application in a container, use:
       ```bash
       docker run -p 5000:5000 salary-predictor
       ```
     - The application will be available at `http://localhost:5000` (or the port you specify).

- **CI/CD Pipeline with Jenkins**:  
   - Continuous Integration and Continuous Deployment (CI/CD) are handled through Jenkins, which automates the process from code commit to deployment.
   - The Jenkins pipeline pulls code from this GitHub repository on every new commit, ensuring that the latest version is always used. It builds the Docker image and deploys the containerized application, streamlining updates and reducing manual intervention.

   - **Setup Instructions**:
     - **Step 1**: Install Jenkins and configure it with Docker.
     - **Step 2**: Set up a Jenkins job to connect with this GitHub repository.
     - **Step 3**: Define the pipeline to automate the build, test, and deployment processes for the Docker container.

   This pipeline provides an automated, reliable workflow for deploying updates to the Salary Predictor application.

## Features

- **Salary Prediction**: Input specific details to get a predicted salary based on the trained model.
- **Automated Deployment**: Jenkins pipeline automatically builds and deploys updates.
- **Version Control**: All project files, including the Dockerfile and Jenkins configuration, are stored and maintained in this GitHub repository.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
2. ** Run with Docker**:
```bash
# Build the Docker image
docker build -t salary-predictor .

# Run the Docker container
docker run -p 5000:5000 salary-predictor
