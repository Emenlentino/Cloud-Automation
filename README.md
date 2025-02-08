# 🌩️ Cloud Automation with Python and Terraform 🚀

Welcome to the **Cloud Automation with Python and Terraform** training course! This course is designed to teach you how to automate cloud resource management using Python and Terraform, providing you with hands-on experience in Infrastructure as Code (IaC) and cloud automation.

---

## 📋 **Course Outline**

### **Week 1: Introduction to Cloud Automation**
- Overview of cloud computing and its benefits.
- Basics of Python for automation.
- Introduction to Terraform and Infrastructure as Code.

### **Week 2: Cloud Provider Fundamentals**
- Setting up an AWS account and managing resources.
- Automating AWS tasks using Python and Boto3.

### **Week 3: Terraform Deep Dive**
- Writing Terraform configurations and workflows.
- Using variables, outputs, and managing Terraform state.

### **Week 4: Advanced Python Automation**
- Implementing error handling and logging in Python scripts.
- Automating complex AWS workflows with Python.

### **Week 5: Terraform and Python Integration**
- Automating Terraform with Python scripts.
- Real-world use case: Deploying a complete cloud infrastructure.

### **Week 6: Final Project and Best Practices**
- Final project: Automating cloud infrastructure deployment.
- Best practices for secure credential management and modularizing configurations.

---

## 🎓 **Benefits of the Course**
1. **Hands-On Learning**: Build real-world cloud solutions with practical projects.
2. **Career Advancement**: Gain in-demand skills for roles like Cloud Automation Engineer or DevOps Engineer.
3. **Efficiency and Scalability**: Automate repetitive tasks and build scalable cloud environments.
4. **Portfolio Building**: Showcase your skills with real-world projects.
5. **Certification**: Earn a certificate to demonstrate your expertise.

---

## 📂 **Course Structure**

### **Project-Based Learning**
- Automate cloud tasks such as creating S3 buckets, launching EC2 instances, and configuring VPCs.
- Use Terraform and Python to manage infrastructure and workflows.

### **Prerequisites**
- Basic knowledge of Python and cloud computing is recommended.
- No prior experience with Terraform is required.

---

## 🚀 **Getting Started**

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/cloud-automation.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your AWS credentials in a secure way (environment variables or AWS Secrets Manager).

4. Start building automation workflows and Terraform configurations!

5. Run the script:

   `streamlit run src/app.py`

---

## 🐳 **Docker Setup**

Run the project in a Docker container for consistent environments:

1. Build the Docker image:
   ```bash
   docker build -t cloud-automation .
   ```

2. Run the Docker container:
   ```bash
   docker run -it -p 8501:8501 -v $(pwd):/app cloud-automation
   ```

3. Access the application at `http://localhost:8501` in your browser.

---

## Project Structure

```bash
cloud_automation/
├── .streamlit/
│   └── secrets.toml                  # Streamlit secrets (AWS credentials, etc.)
├── src/                              # Main source code for Streamlit app
│   ├── app.py                        # Streamlit app file (your current script)
│   ├── terraform/                    # Terraform configuration files (e.g., main.tf, variables.tf)
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars.json
│   └── utils/                         # Utility functions
│       ├── aws.py                    # Functions for AWS interaction (e.g., boto3)
│       ├── logging.py                # Custom logging setup
│       ├── background.py             # Functions for background images and styling
├── assets/                           # Store images, icons, or any other assets
│   └── background.png                # Example background image
├── requirements.txt                  # Python dependencies (e.g., streamlit, boto3, rich, etc.)
└── README.md                         # Project documentation

```

## 📚 **Resources**
- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [AWS Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Python Logging Best Practices](https://docs.python.org/3/library/logging.html)
- [Rich Library Documentation](https://rich.readthedocs.io/en/stable/)

---

## 🤝 **Contributing**
We welcome contributions to this repository! Feel free to submit issues or pull requests to improve the course content.

---

## 📧 **Contact**
If you have any questions, reach out to us at: **emenlentino@gmail.com**.

---

Happy Automating! 🎉
