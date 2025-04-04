pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  // Use Python 3.9 Docker image
            args '-u root:root'  // Optional: Run as root for package installation
        }
    }

    environment {
        PROJECT_NAME = "FlaskApp"
        IMAGE_NAME = "flask-app"
        ARTIFACTORY_URL = "your-artifactory-url"  // Replace with your Artifactory URL
        ARTIFACTORY_REPO = "your-repository-name"  // Replace with your Artifactory repo
        ARTIFACTORY_CREDENTIALS = credentials('artifactory-credentials-id')  // Artifactory credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from the Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies inside the Docker container using pip
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests using pytest
                    sh 'pytest test_app.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t ${IMAGE_NAME}:latest .'
                }
            }
        }

        stage('Push Docker Image to Artifactory') {
            steps {
                script {
                    // Log in to Artifactory
                    sh "docker login ${ARTIFACTORY_URL} -u ${ARTIFACTORY_CREDENTIALS_USR} -p ${ARTIFACTORY_CREDENTIALS_PSW}"

                    // Tag the image with the Artifactory repository URL
                    sh "docker tag ${IMAGE_NAME}:latest ${ARTIFACTORY_URL}/${ARTIFACTORY_REPO}/${IMAGE_NAME}:latest"

                    // Push the image to Artifactory
                    sh "docker push ${ARTIFACTORY_URL}/${ARTIFACTORY_REPO}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'  // Deploy only from the main branch
            }
            steps {
                script {
                    // Deploy step (can be customized based on your deployment process)
                    echo "Deploying ${env.PROJECT_NAME} to production..."
                    sh './deploy.sh'  // Assuming you have a custom deploy script
                }
            }
        }
    }

    post {
        success {
            echo "Build, test, Docker image build, and deployment were successful!"
        }
        failure {
            echo "Build, test, Docker image build, or deployment failed. Please check the logs."
        }
    }
}

