# Simple Voting System — v1, v2, v3

A beginner-friendly Flask project designed for the assignment:
- Developed in VS Code
- Versioned in Git/GitHub
- Built and pushed with a Jenkins pipeline
- Containerized as Docker tags `v1`, `v2`, `v3`
- Deployed as three Kubernetes Deployments and Services on different localhost ports

## What each version does
- **v1** (`v1/`): Add candidates and view the candidate list.
- **v2** (`v2/`): Add candidates and cast votes.
- **v3** (`v3/`): Add candidates, cast votes, and display vote counts/results.

> This is a learning/demo app. Data is stored in memory, so votes reset when the container restarts. Do not use it for real elections.

## 1. Run locally in VS Code
Open this folder in VS Code. In a terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python v3/app.py
```

Open `http://127.0.0.1:5000`.

To run v1 or v2 instead, stop the server with Ctrl+C and run `python v1/app.py` or `python v2/app.py`.

## 2. GitHub versioning suggestion
Create a GitHub repository named `simple-voting-system`. Keep `main` as v1, and use branches for the next versions:
```powershell
git init
git add .
git commit -m "v1: add candidates"
git branch v2-voting
git branch v3-results
```
To make each branch contain its own version, switch to the branch and commit the corresponding version changes. You can also use three separate commits on `main` if your instructor accepts separate commits instead of branches.

## 3. Jenkins prerequisites
Install/configure the Jenkins Git plugin and Pipeline plugin. Ensure the Jenkins agent can run `git`, `docker`, and `kubectl`, and can access your Kubernetes cluster.

In **Manage Jenkins → Credentials**, add a **Username with password** credential:
- ID: `dockerhub-creds`
- Username: your Docker Hub username
- Password: your Docker Hub access token (recommended)

In `Jenkinsfile`, replace `sahithi3377/simple-voting-system` with your own Docker Hub repository if needed. Configure the job to use this repository's `Jenkinsfile`.

The pipeline uses Windows `bat` commands, matching a Windows Jenkins installation. If your Jenkins agent runs Linux, change `bat` steps to `sh`.

## 4. Docker build/push commands (manual fallback)
Replace `YOUR_DOCKERHUB_USERNAME`:
```powershell
docker login
docker build -t YOUR_DOCKERHUB_USERNAME/simple-voting-system:v1 .\v1
docker build -t YOUR_DOCKERHUB_USERNAME/simple-voting-system:v2 .\v2
docker build -t YOUR_DOCKERHUB_USERNAME/simple-voting-system:v3 .\v3
docker push YOUR_DOCKERHUB_USERNAME/simple-voting-system:v1
docker push YOUR_DOCKERHUB_USERNAME/simple-voting-system:v2
docker push YOUR_DOCKERHUB_USERNAME/simple-voting-system:v3
```

## 5. Deploy to Kubernetes
Edit `k8s/deployments-services.yaml` and replace `sahithi3377` with your Docker Hub username if necessary. Ensure Docker Desktop Kubernetes is running, then:
```powershell
kubectl apply -f .\k8s\deployments-services.yaml
kubectl get deployments
kubectl get pods
kubectl get services
```

Open:
- v1: `http://localhost:30081`
- v2: `http://localhost:30082`
- v3: `http://localhost:30083`

If the images were pushed under a different Docker Hub username, update the image names in the Kubernetes YAML first.
