# 🔁 Module 4: Jenkins Job Types & Groovy Pipelines

## 🎯 Objective
Learn the different job types in Jenkins, why pipelines are preferred, and how Groovy is used to define pipeline logic.

---

## 🧾 Job Types in Jenkins

### 1️⃣ **Freestyle Jobs**
- Configured via the Jenkins UI (click-through interface).
- Good for very simple tasks.
- Limited flexibility, no version control.

### 2️⃣ **Pipeline Jobs** (⚡ Preferred)
- Defined using **code** in a `Jenkinsfile`.
- Written in **Groovy DSL (Domain Specific Language)**.
- Stored in your Git repository = version-controlled CI/CD logic.

---

## 🧠 Why Use Pipelines?

- Reproducible and shareable (stored in Git).
- Supports complex workflows (branches, parallel stages, conditionals).
- Easier to maintain in teams.
- More scalable and secure.

---

## 🧑‍💻 What is Groovy?

**Groovy** is a powerful scripting language that runs on the Java Virtual Machine (JVM). It’s similar to Java but more concise and dynamic.

Jenkins uses **Groovy-based DSLs** for defining pipelines.

You don’t need to be a Groovy expert, but understanding the basics helps you customize pipelines.

---

## 🔤 Groovy Basics for Jenkins

### ✅ Variables
```groovy
def name = "DataPipeline"
int count = 5
```

### ✅ Functions
```groovy
def greet(name) {
  echo "Hello, ${name}!"
}
```

### ✅ Conditionals
```groovy
if (env.BRANCH_NAME == 'main') {
  echo "Deploying to production"
} else {
  echo "Running tests only"
}
```

### ✅ Loops
```groovy
for (int i = 0; i < 3; i++) {
  echo "Build step ${i}"
}
```

---

## 📜 Basic Declarative Pipeline Example
```groovy
pipeline {
  agent any

  environment {
    PROJECT_NAME = "DataPlatform"
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/your-repo/data-project.git'
      }
    }

    stage('Build') {
      steps {
        echo "Building ${env.PROJECT_NAME}"
      }
    }

    stage('Test') {
      steps {
        sh 'pytest tests/'
      }
    }

    stage('Deploy') {
      when {
        branch 'main'
      }
      steps {
        echo "Deploying to production..."
      }
    }
  }
}
```

---

## 🛠️ Scripted vs Declarative Pipelines

| Type         | Description                                     | Use When...                           |
|--------------|--------------------------------------------------|----------------------------------------|
| Declarative  | High-level, structured syntax (recommended)     | Most cases—easier to learn and maintain |
| Scripted     | Full Groovy syntax (flexible but complex)       | You need full control/logic handling   |

---

## 💡 Example: Scripted Pipeline
```groovy
node {
  stage('Init') {
    echo 'Starting build...'
  }

  stage('Build') {
    sh 'make build'
  }

  stage('Test') {
    sh 'pytest tests/'
  }

  if (env.BRANCH_NAME == 'main') {
    stage('Deploy') {
      echo 'Deploying to production...'
    }
  }
}
```

---

## 📦 Summary

| Concept             | Description                                           |
|---------------------|-------------------------------------------------------|
| Groovy              | Language used to script Jenkins pipelines             |
| Declarative Pipeline| Easier, structured syntax for most common pipelines   |
| Scripted Pipeline   | Full Groovy power for custom logic-heavy pipelines    |
| Jenkinsfile         | A Groovy script that lives in your repo and defines CI/CD |

> 💬 Pipelines let you treat your automation like code. That means version control, review, reuse—and ultimately, **safer and faster software delivery**.

