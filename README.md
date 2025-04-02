# Overengineered Cloud Resume

Welcome to my Overengineered Cloud Resume!

This project is not just a simple resume—it's a showcase of my expertise in cloud computing, DevOps, and full-stack development. I wanted to challenge myself by designing a highly scalable, cloud-native architecture while integrating industry best practices like Infrastructure as Code (IaC), CI/CD pipelines, serverless computing, and cloud monitoring.

The goal? To over-engineer a simple resume into a fully automated, multi-cloud deployable, and cost-optimized web application just to get a feeling of building something complex.

This project is also designed to be modular and reusable, making it a great starting point for anyone who wants to build their own cloud-hosted resume or portfolio.

My journey into cloud computing began with an unexpected challenge—I was a struggling college student who couldn't afford a high-end gaming rig. Gaming had always been my passion, but the steep hardware costs were a roadblock. Then, in 2018, I stumbled upon GeForce Now's early access program, a cloud gaming service that allowed users to stream high-performance games on virtually any device.

Witnessing firsthand how cloud technology could seamlessly bridge the gap between affordability and performance was eye-opening. The realization hit me—computing power was undergoing the same transformation as electricity did in the early 1900s, when every building required its own generator before the advent of centralized grids. Cloud computing had the potential to democratize access to powerful resources.

Inspired by this, I decided to invest in Nvidia stock when the cloud gaming service became publicly available—a decision that turned into an unexpected success. As AI continues to advance and demand more intensive computing resources, I am more convinced than ever that cloud computing will become even more prevalent, driving innovation and making high-performance computing accessible to all.

Thank you for visiting my Over-Engineered Cloud Resume Challenge!

---

## Links

Feel free to connect or provide feedback:

- **The Cloud Resume**: [randalldev.link](https://randalldev.link/)
- **LinkedIn**: [linkedin.com/in/randall-y-liao](https://linkedin.com/in/randall-y-liao)
- **GitHub**: [randall-liao](https://github.com/randall-liao)
- **Cloud Resume React Frontend**: [GitHub Repo](https://github.com/randall-liao/react-frontend-cloud-resume)

---

---

## Table of Contents

1. [Overview](#overview)
2. [Roadmap](#roadmap)
3. [Architecture](#architecture)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Challenges and Learnings](#challenges-and-learnings)
7. [Contact](#contact)

---

## Overview

This project serves as my cloud-based resume hosted entirely on the cloud, using a multi-layered architecture. It demonstrates:

- Cloud-native web hosting.
- Serverless backend services.
- Infrastructure as Code (IaC).
- CI/CD pipelines.
- Monitoring and analytics.
- Easily portable and reusable by others.

---

## Roadmap

### Stage 0: Build and Deploy the Resume

1. **Certification**

 :white_check_mark: Finished! Check out courses that helped me pass the certification exam: [Coursera: AWS Cloud Solutions Architect Professional Certificate](https://www.coursera.org/programs/sobma/professional-certificates/aws-cloud-solutions-architect)


   - I'm an AWS Certified Solution Architect now! [AWS Certified Solution Architect](https://www.credly.com/badges/cf3fc6ea-c18c-4bcb-95f4-a58d0cc770de/linked_in_profile)

2. **Frontend Development** [(Blog Post)](https://TODO)[(Tutorial)](https://TODO)

 :white_check_mark: Finished! Check out the [GitHub Repo](https://github.com/randall-liao/react-frontend-cloud-resume) for the frontend code.

   - A React web application
   - Cross-platform compatible website

3. **Static Website Deployment** [(Blog Post)](https://TODO)[(Tutorial)](https://TODO)

 :white_check_mark: Finished! Check out [my cloud resume](https://randalldev.link/)

   - Host static resources on an Amazon S3 static website.
   - Enable HTTPS using Amazon CloudFront.
   - Point a custom domain name to the CloudFront distribution using Route 53 or another DNS provider.

4. **Infrastructure as Code (IaC)**

   - Use an IaC tool such as AWS SAM or Terraform to define and deploy all infrastructure.
   - Ensure the project is modular and reusable for other users with clear instructions.

5. **Visitor Counter**

   - Add a visitor counter using ReactApp.
   - All backend api should be serverless to reduce cost.
   - Store visitor data in DynamoDB.

### Stage 1: Enhanced Features

1. **Security Enhancements**

   - Add a reCAPTCHA test to prevent misuse and leaks of personal information.

2. **User Tracking**

   - Implement user tracking for analytics using a serverless solution.

3. **Future Expansion**

   - Plan and integrate the resume as the first step towards a personal website, such as a self-hosted blog or portfolio.

### Stage 2: Cost Optimization and Multi-Cloud Compatibility

1. **Optimize Hosting Costs**

   - Explore free-tier options from various cloud providers to minimize hosting costs.
   - Transition static site hosting and backend functions to cost-effective alternatives while maintaining performance.

2. **Multi-Cloud Compatibility**

   - Make the project deployable across multiple cloud platforms (e.g., AWS, Azure, Google Cloud).
   - Use provider-agnostic IaC tools like Terraform to streamline deployments.

---

## Architecture

The solution follows a multi-tier architecture:

1. **Frontend**: A responsive resume hosted on a static site platform.
2. **Backend**: A serverless function to record and display visitor counts.
3. **Database**: A managed NoSQL database to store visitor data.
4. **Infrastructure**: Automated deployment using IaC tools.



---

## Features

- **Responsive Design**: Optimized for desktop and mobile viewing.
- **Visitor Count Tracking**: Displays live visitor counts powered by serverless functions and a managed database.
- **Fully Automated Deployment**: Utilizes CI/CD pipelines for seamless updates.
- **Cloud-Native Monitoring**: Integrates cloud monitoring and logging services.

---

## Technologies Used

### Frontend

- HTML, CSS, JavaScript
- Framework: [React/Vue/Angular] (Choose the framework used)
- Hosting: AWS S3 + CloudFront / Azure Static Web Apps / GCP Cloud Storage

### Backend

- Serverless Functions: AWS Lambda / Azure Functions / Google Cloud Functions
- Runtime: Node.js / Python

### Database

- DynamoDB / Firebase Realtime Database / Firestore

### Infrastructure

- Infrastructure as Code: Terraform / AWS CloudFormation / Azure Bicep
- CI/CD: GitHub Actions / GitLab CI / Azure DevOps Pipelines

### Monitoring

- CloudWatch / Azure Monitor / Google Cloud Operations Suite

---

## Setup

Follow these steps to deploy the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo-url
   cd cloud-resume
   ```

2. **Frontend Deployment**

   - Configure your static site hosting.
   - Update the frontend environment variables as required.
   - Build and deploy the frontend.

3. **Backend Deployment**

   - Deploy the serverless function using the IaC tool.
   - Configure API Gateway/Endpoint for the function.

4. **Database Setup**

   - Set up the managed database.
   - Seed initial data if required.

5. **CI/CD Configuration**

   - Connect the repository to the CI/CD tool.
   - Ensure pipeline configurations are correct.

---

## Challenges and Learnings

- **Challenge**: Balancing simplicity with over-engineering.
- **Solution**: Carefully documented all steps and ensured scalability.
- **Key Learning**: Mastering cloud services, serverless architecture, and automated pipelines.





