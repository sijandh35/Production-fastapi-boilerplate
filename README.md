Production FastAPI Boilerplate

A production-ready FastAPI boilerplate designed for scalable, maintainable, and performant API development.
Features

    FastAPI: High-performance Python framework for building APIs.
    Docker: Containerized development and production environment.
    Environment Configuration: Easy environment setup with .env files.
    Scalable Architecture: Clean and modular design for enterprise use.
    Deployment Ready: Seamless container orchestration with Docker Compose.

Getting Started
1. Clone the Repository

git clone <repository-url>
cd production-fastapi-boilerplate

2. Set Up Environment Variables

Copy the example environment file and modify it to match your configuration:

cp envs/env_sample .env

3. Set Up Docker Configuration

Copy the example docker-compose file and make any necessary adjustments:

cp docker-compose.yml.sample docker-compose.yml

4. Build and Run the Application

Use Docker Compose to build and start the application:

docker compose up

The application will be accessible at http://localhost:<port> (default: 8045).