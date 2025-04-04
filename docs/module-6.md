# 🔌 Trigger Jenkins Jobs Externally with Python

## 🎯 Objective
In this module, you'll learn how to trigger Jenkins jobs **externally** using a **Python script**. Jenkins provides a **REST API** that allows you to interact with Jenkins jobs programmatically. By using this API, you can trigger builds, pass parameters, and even retrieve build results.

---

## 🧰 Prerequisites

1. **Jenkins instance running** and accessible.
2. **Jenkins API token** for authentication.
3. A **Jenkins job** configured and ready to be triggered.
4. **Python** installed, with the `requests` library.

---

## 🔧 How Jenkins API Works

Jenkins exposes a REST API that can be used to trigger jobs, get job status, and even retrieve logs. The typical structure to trigger a build via the API looks like this:

> POST /job/<JOB_NAME>/build


Where:
- `<JOB_NAME>` is the name of the Jenkins job you want to trigger.

For jobs that require parameters, you can use this API endpoint:

> POST /job/<JOB_NAME>/buildWithParameters?PARAM1=value1&PARAM2=value2


---

## 🐍 Python Script to Trigger Jenkins Job

Below is a Python script using the `requests` library that triggers a Jenkins job:

#### `trigger_jenkins_job.py`
```python
import requests
from requests.auth import HTTPBasicAuth

# Jenkins details
jenkins_url = "http://your-jenkins-server-url"  # Jenkins server URL
job_name = "your-jenkins-job-name"  # The name of the job you want to trigger
user = "your-jenkins-username"  # Your Jenkins username
api_token = "your-jenkins-api-token"  # Your Jenkins API token (can be found in Jenkins user settings)

# Optional: Parameters to pass to the Jenkins job (if required)
params = {
    "PARAM1": "value1",
    "PARAM2": "value2"
}

# Construct the URL for triggering the job
trigger_url = f"{jenkins_url}/job/{job_name}/buildWithParameters"

# Trigger the Jenkins job with authentication
response = requests.post(trigger_url, params=params, auth=HTTPBasicAuth(user, api_token))

# Check if the request was successful
if response.status_code == 201:
    print(f"Successfully triggered the job: {job_name}")
else:
    print(f"Failed to trigger the job. Status code: {response.status_code}")
    print(f"Response: {response.text}")
```

## 🧑‍💻 Explanation of the Python Script

1. **Jenkins Server URL**:  
   Replace `http://your-jenkins-server-url` with the actual URL of your Jenkins server. Make sure that the Jenkins server is accessible from the machine where you're running the Python script.

2. **Job Name**:  
   Replace `your-jenkins-job-name` with the name of the Jenkins job you want to trigger. You can find the job name in the Jenkins dashboard.

3. **Authentication**:  
   This script uses **Basic Authentication** to authenticate with Jenkins. Replace `your-jenkins-username` and `your-jenkins-api-token` with your actual Jenkins username and API token. You can find your API token in the Jenkins user settings.

4. **Optional Parameters**:  
   If your Jenkins job requires parameters, you can pass them in the `params` dictionary. This is necessary for jobs like pipelines that take input parameters.

5. **Triggering the Job**:  
   The script sends a **POST request** to the `/buildWithParameters` endpoint of the Jenkins REST API. It includes the parameters if they are provided. A successful trigger will return a `201` status code, which means the job was initiated successfully.

6. **Error Handling**:  
   If the request fails (e.g., due to incorrect credentials or the job not being found), the script will print the HTTP status code and the response message to help debug the issue.

---

## 📝 Steps to Run the Script

1. **Install Dependencies**:  
   Ensure you have Python installed and the `requests` library available. You can install it using pip if it's not already installed:
   ```bash
   pip install requests
   ```

2. **Update the Script**:  
   Modify the script with your Jenkins URL, job name, and authentication credentials.

3. **Run the Script**:  
   Execute the script to trigger the Jenkins job:
   ```bash
   python trigger_jenkins_job.py
   ```

4. **Verify**:  
   After running the script, check the Jenkins UI to verify that the job has been triggered. You should also see the updated status of the job.

---

## ✅ Summary

| Concept             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Jenkins REST API    | Allows external applications to interact with Jenkins (e.g., triggering jobs). |
| `requests` Library  | Python library used for making HTTP requests to interact with the Jenkins API. |
| `buildWithParameters` | Endpoint to trigger Jenkins jobs with parameters.                           |
| Authentication      | The script uses **Basic Authentication** with Jenkins credentials.          |

> 💬 By using the **Jenkins REST API** and a simple **Python script**, you can automate the process of triggering Jenkins jobs externally, integrating Jenkins with other tools, or scheduling builds programmatically.

---

This module equips you with the necessary knowledge and practical script to trigger Jenkins jobs from external systems or applications.



