from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to the Dockerized Flask App!'


@app.route('/Vaibhav_Karkute')
def vaibhav_karkute():
    return 'Hello, I am Vaibhav Karkute, a DevOps Engineer at TCS with expertise in Kubernetes, monitoring tools (Grafana, Elastic, Dynatrace), Docker, Ansible, Terraform, etc. I am passionate about building scalable applications and exploring new technologies.'


@app.route('/info')
def info():
    return 'This is a simple Flask application running inside a Docker container.'  


@app.route('/health')
def health_check():
    return 'Health check OK!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)