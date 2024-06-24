# Microservices-based E-Commerce System

This project implements a microservices architecture for a simple e-commerce application using Python with Flask. It includes modules for user authentication, product management, and order processing, ensuring scalability, concurrency control, and high availability.

## Features

- **Microservices Architecture**: 
  - User Authentication Service
  - Product Management Service
  - Order Processing Service
  - Communication via RESTful APIs

- **Concurrency Control**:
  - Optimistic locking for product management to handle concurrent data access.

- **Clustering and High Availability**:
  - Deployment across multiple nodes/containers to ensure high availability.

- **Database Integration**:
  - MySQL database for storing user profiles, product catalogs, and order histories.
  - Efficient schema design and database operations.

- **Authentication and Authorization**:
  - Secure user authentication using scrypt for encryption
    
## Technologies Used

- Python
- Flask
- MySQL
- Docker (for containerization)
- Docker-compose (for deployment testing)
- Kubernetes (k8s)
- Git (for version control)

## Getting Started

To get a local copy up and running, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ecommerce-microservices.git
   cd ecommerce-microservices
  
2. Start services with Docker Compose:

  ```bash
  docker-compose up -d
  ```

3. Access APIs:

    Use tools like Postman to interact with the APIs exposed by each microservice.

4. Stop and remove containers:

  ```bash
  docker-compose down
  ```

   
