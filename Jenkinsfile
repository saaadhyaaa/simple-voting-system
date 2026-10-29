pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'saadhyaprabu/agileassessment'
        K8S_MANIFEST = 'k8s/deployments-services.yaml'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                bat 'docker build -t %DOCKERHUB_REPO%:v1 v1'
                bat 'docker build -t %DOCKERHUB_REPO%:v2 v2'
                bat 'docker build -t %DOCKERHUB_REPO%:v3 v3'
            }
        }

        stage('Login and Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credsss',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    bat 'echo %DOCKERHUB_PASSWORD%| docker login -u %DOCKERHUB_USERNAME% --password-stdin'
                    bat 'docker push %DOCKERHUB_REPO%:v1'
                    bat 'docker push %DOCKERHUB_REPO%:v2'
                    bat 'docker push %DOCKERHUB_REPO%:v3'
                }
            }
        }


        stage('Deploy to Kubernetes') {
            steps {
                withEnv(['KUBECONFIG=C:/Users/Yadam Sahithi Reddy/.kube/config']) {
                    bat 'echo Checking Kubernetes configuration...'
                    bat 'if not exist "%KUBECONFIG%" (echo ERROR: Kubernetes config file not found & exit /b 1)'
                    bat 'kubectl config current-context'
                    bat 'kubectl get nodes'
                    bat 'kubectl apply -f k8s/deployments-services.yaml'
                    bat 'kubectl rollout status deployment/voting-v1 --timeout=120s'
                    bat 'kubectl rollout status deployment/voting-v2 --timeout=120s'
                    bat 'kubectl rollout status deployment/voting-v3 --timeout=120s'
                }
            }
        }
    }

    post {
        success {
            echo 'All three versions were built, pushed, and submitted to Kubernetes.'
        }
        failure {
            echo 'Pipeline failed. Open the failed stage in Console Output and check its first error.'
        }
    }
}
