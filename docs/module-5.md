# 🚀 Module 5: Basic Workflow (CI/CD in Action)

## 🎯 Objective
Learn how Jenkins can automate the process of building, testing, and deploying your applications and pipelines using **CI/CD**.

---

## 🛠️ CI/CD Workflow in Jenkins

The Jenkins pipeline automates the flow from **code commit → build → test → deploy**. This cycle is crucial for continuous delivery (CD) and continuous integration (CI). Jenkins uses **Jenkinsfiles** (Groovy-based) to define the exact steps.

---

## 🔄 Continuous Integration (CI)

### Steps:
1. **Developer pushes code** to the Git repository (e.g., GitHub, GitLab).
2. **Jenkins checks for changes** in the repository.
3. If new changes are detected:
   - Jenkins **checks out the code**.
   - It **builds** the application (compiling code, building Docker images, etc.).
   - It runs **unit tests** to ensure nothing is broken.
4. If the build fails, Jenkins sends an alert (email/Slack), and the developers can quickly fix the issue.

> **CI helps detect bugs early** in the development process, making it easier and faster to fix them.

---

## 🚀 Continuous Delivery (CD)

### Steps:
1. After successful builds and tests, Jenkins can **deploy the application** to a staging environment for further testing or validation.
2. This step is **automated** so that any time code is updated, it’s ready to go live.
3. **Optional Manual Approval**: You can configure Jenkins to wait for manual approval before deploying to production.

> **CD allows you to continuously deliver working code** to testing or production environments with minimal human intervention.

---

## 🧩 CI/CD Pipeline Example

Here’s a **basic declarative Jenkins pipeline** that defines CI/CD steps:

### Jenkinsfile
```groovy
pipeline {
    agent {
        docker {
            image 'python:3.9'  // Using Python 3.9 Docker image
            args '-u root:root'  // Optional: Run as root for package installation
        }
    }

    environment {
        PROJECT_NAME = "MyPythonApp"
        IMAGE_NAME = "my-python-app"
        ARTIFACTORY_URL = "your-artifactory-url"
        ARTIFACTORY_REPO = "your-repository-name"
        ARTIFACTORY_CREDENTIALS = credentials('artifactory-credentials-id')  // Jenkins credentials ID for Artifactory
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
                    // Install dependencies inside the Python Docker container using pip
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests using pytest
                    sh 'pytest tests/'
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
                    // Deploy step (can be any deployment logic you want)
                    echo "Deploying ${env.PROJECT_NAME} to production..."
                    sh './deploy.sh'  // Assuming you have a deploy script
                }
            }
        }
    }

    post {
        success {
            echo "Build and deploy were successful!"
        }
        failure {
            echo "Build or deploy failed. Please check the logs."
        }
    }
}
```

---

## 🖼️ CI/CD Pipeline Diagram

> 📌 *Insert diagram of the flow: Developer commits code → Jenkins builds → Jenkins tests → Jenkins deploys*

---

## 🧠 Key Concepts to Remember

- **Jenkinsfile**: A Groovy script that defines your CI/CD pipeline.
- **Stages**: Each distinct phase of the pipeline, such as checkout, build, test, and deploy.
- **Steps**: The individual actions taken during a stage (e.g., running a shell command).
- **Post Actions**: Defined for actions that should happen after the pipeline completes, like notifications or cleanup.

---

## ✅ Benefits of CI/CD with Jenkins

- **Faster feedback** on changes (detect errors early).
- **Automated testing** ensures code quality.
- **Consistency** across environments (dev, staging, production).
- **Faster time to market** with frequent, smaller releases.
- **Minimized human error** in the deployment process.

---

## 📦 Summary

| Concept           | Description                                          |
|-------------------|------------------------------------------------------|
| Continuous Integration | Detects issues early by integrating changes continuously. |
| Continuous Delivery  | Automates deployment, making code always ready for release. |
| Jenkins Pipeline   | Code-based workflow that automates CI/CD tasks.      |
| Stages             | Define phases in a pipeline (e.g., build, test, deploy). |
| Steps              | Actions performed within each stage (e.g., running tests). |

> CI/CD isn’t just about automating builds. It’s about **creating a culture** of continuous improvement, faster delivery, and higher quality.
AgentsAgents
