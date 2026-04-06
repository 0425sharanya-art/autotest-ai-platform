# AutoTest AI Platform

AI-powered microservices-based test automation platform.

## Architecture

API Gateway → Test Runner → AI Test Generator → Defect Analyzer

## Features

- Automated API testing
- Selenium UI testing
- AI test case generation
- AI failure root cause analysis
- Microservices architecture
- Docker containerization
- React dashboard

## Tech Stack

Python  
FastAPI  
Docker  
Pytest  
Selenium  
React  
Ollama (LLM)

## Run Locally

Start services

docker-compose up --build

API Gateway

http://localhost:8000

Run tests

POST /run-tests

## Future Improvements

- Self-healing locators
- Visual testing
- Performance testing with k6
- Security scanning with OWASP ZAP
