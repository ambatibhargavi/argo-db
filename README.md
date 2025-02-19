##### Flask DynamoDB CRUD App
![ScreenRecording2025-02-19at15 54 03-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/66750777-83d3-4c23-9bca-1492329e0276)


This project is a Python Flask application that interacts with AWS DynamoDB, enabling CRUD operations via CLI commands and a web interface. The application is containerized using Docker, deployed on Kubernetes, and managed using ArgoCD.

##### Features

Perform CRUD operations on DynamoDB using CLI commands.
View database records through a simple HTML page on localhost:5000.
Dockerized application with an image hosted on DockerHub.
Kubernetes deployment using deployment.yaml and service.yaml.
Continuous deployment with ArgoCD.

##### Prerequisites

Python 3.x
Flask
AWS DynamoDB
Docker
Kubernetes (Minikube/K8s cluster)
ArgoCD
Git

#### Installation and Usage

1. Clone the Repository
             git clone https://github.com/ambatibhargavi/argo-db.git
             cd https://github.com/ambatibhargavi/argo-db.git
2. Run the Flask Application Locally
              python app.py
Access the web interface at http://localhost:5000.
<img width="477" alt="Screenshot 2025-02-17 at 18 55 32" src="https://github.com/user-attachments/assets/cd44d190-335a-4141-88d5-a05a45e1802f" />
<img width="823" alt="Screenshot 2025-02-18 at 21 44 24" src="https://github.com/user-attachments/assets/2033cf19-ec58-4da6-982d-d15c64a94c12" />

3. Dockerization
              docker build -t <dockerhub-username>/flask-dynamodb:latest .
              docker push <dockerhub-username>/flask-dynamodb:latest
   <img width="1440" alt="Screenshot 2025-02-17 at 20 04 03" src="https://github.com/user-attachments/assets/0543c278-8500-411e-bd6f-3fa71632eb7f" />
   
4. Deploy on Kubernetes
              kubectl apply -f deployment.yaml
              kubectl apply -f service.yaml

Check the running pods:
kubectl get pods
<img width="733" alt="Screenshot 2025-02-18 at 08 33 54" src="https://github.com/user-attachments/assets/3cdf7e48-bc48-4754-ba1c-0c70b2601e97" />

             kubectl apply -f deployment.yaml
             kubectl apply -f service.yaml
<img width="912" alt="Screenshot 2025-02-19 at 18 15 36" src="https://github.com/user-attachments/assets/568ff5dc-f7cd-4295-b1fb-1e1eb70b729c" />
5. Deploy with ArgoCD
Apply ArgoCD Configuration
              kubectl apply -f argo.yaml
<img width="758" alt="Screenshot 2025-02-18 at 16 25 41" src="https://github.com/user-attachments/assets/5e0a4166-0a84-401b-a059-8db343abae50" />
<img width="945" alt="Screenshot 2025-02-19 at 07 36 08" src="https://github.com/user-attachments/assets/857c0e36-5110-4882-abe0-9e704be25428" />
<img width="726" alt="Screenshot 2025-02-18 at 16 05 14" src="https://github.com/user-attachments/assets/78531f9b-0b92-4d6d-9f86-1fe22649038c" />
<img width="901" alt="Screenshot 2025-02-18 at 16 15 30" src="https://github.com/user-attachments/assets/10e5ee9e-bc52-453c-9d20-2e0f510a78e6" />

#### Repository Structure

├── app.py              # Flask application logic
├── templates/          # HTML files for UI
├── Dockerfile          # Docker image configuration
├── requirements.txt    # Python dependencies
├── manifests / deployment.yaml     # Kubernetes deployment file
├── service.yaml        # Kubernetes service file
├── argo.yaml           # ArgoCD deployment configuration
├── README.md           # Project documentation

#### Crud operations using cli commands

<img width="611" alt="Screenshot 2025-02-17 at 18 51 49" src="https://github.com/user-attachments/assets/2d12d9fe-9784-43e0-8ce4-ff143dd44e8b" />
<img width="1110" alt="Screenshot 2025-02-17 at 18 54 08" src="https://github.com/user-attachments/assets/fc6c9d15-ff1b-49e3-8a42-778e285537f0"/>
<img width="810" alt="Screenshot 2025-02-17 at 18 54 18" src="https://github.com/user-attachments/assets/ebde516f-ba34-4bed-ac3c-b64ba0ff90b0" />
<img width="565" alt="Screenshot 2025-02-17 at 18 58 12" src="https://github.com/user-attachments/assets/cb11ff79-3694-4eaa-9f08-0ce342dd7228" />

Contributing

Feel free to fork this repository and create a pull request for any improvements.





