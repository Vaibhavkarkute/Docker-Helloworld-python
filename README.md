# Dockerized Flask App

This project demonstrates how to run a simple Flask application inside a Docker container.

## Features

- Home route: `/`  
  Returns a welcome message.

- About route: `/Vaibhav_Karkute`  
  Returns information about Vaibhav Karkute.

- Info route: `/info`  
  Returns details about the app.

- Health check route: `/health`  
  Returns health status.

## How to Run

1. **Build the Docker image:**
   ```bash
   docker build -t python-app .
   ```

2. **Run the container (map port 5000 or another available port):**
   ```bash
   docker run -d -p 5000:5000 python-app
   ```
   If port 5000 is busy, use another port:
   ```bash
   docker run -d -p 5050:5000 python-app
   ```

3. **Access the app in your browser:**
   - Home: [http://localhost:5000/](http://localhost:5000/)
   - About: [http://localhost:5000/Vaibhav_Karkute](http://localhost:5000/Vaibhav_Karkute)
   - Info: [http://localhost:5000/info](http://localhost:5000/info)
   - Health: [http://localhost:5000/health](http://localhost:5000/health)

## Files

- `helloworld.py` : Main Flask application.
- `Dockerfile` : Instructions to build the Docker image.
- `README.md` : Project documentation.

## Author

Vaibhav Karkute  
DevOps Engineer
