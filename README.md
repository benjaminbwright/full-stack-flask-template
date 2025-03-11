# Full-Stack FastAPI and React Template

A modern, production-ready template for building full-stack applications with FastAPI and React. This template provides a modular structure with Docker support for both development and production environments.

## Features

- 🚀 FastAPI backend for high-performance API development
- ⚛️ React frontend with modern tooling
- 🐳 Docker and Docker Compose support for development
- 📦 Separate production-ready Dockerfiles for cloud deployment
- 📁 Modular project structure for both frontend and backend
- 🔍 Example TODO list CRUD implementation
- 📝 Auto-generated API documentation (Swagger/OpenAPI)
- ✨ Clean, maintainable architecture
- 🔒 Type safety with Pydantic models and TypeScript

## Quick Start with Docker (Development)

### Prerequisites

- Docker
- Docker Compose

### Development Setup

1. Clone the template:

   ```bash
   git clone https://github.com/yourusername/full-stack-fastapi-template.git
   cd full-stack-fastapi-template
   ```

2. Start the development environment:

   ```bash
   docker-compose up
   ```

3. Access the applications:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Manual Setup (Without Docker)

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Project Structure

```
full-stack-fastapi-template/
├── docker-compose.yml          # Development Docker Compose configuration
├── backend/
│   ├── Dockerfile             # Production backend Dockerfile
│   ├── Dockerfile.development # Development backend Dockerfile
│   ├── main.py               # Application entry point
│   ├── requirements.txt      # Python dependencies
│   ├── models/               # Data models
│   └── routes/               # API routes
├── frontend/
│   ├── Dockerfile           # Production frontend Dockerfile
│   ├── Dockerfile.development # Development frontend Dockerfile
│   ├── package.json
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/          # Page components
│   │   └── services/       # API services
│   └── public/             # Static assets
```

## Production Deployment

The template includes separate Dockerfiles for production deployment of both frontend and backend services. This allows for independent scaling and deployment of each service in cloud environments.

### Building Production Images

1. Backend:

   ```bash
   docker build -t myapp-backend ./backend
   ```

2. Frontend:
   ```bash
   docker build -t myapp-frontend ./frontend
   ```

### Environment Variables

- Backend:

  - `DATABASE_URL`: Database connection string
  - `SECRET_KEY`: Application secret key
  - Additional environment variables as needed

- Frontend:
  - `REACT_APP_API_URL`: Backend API URL
  - Additional environment variables as needed

## API Endpoints

The template includes a complete TODO list API:

- `GET /api/todos` - List all todos
- `POST /api/todos` - Create a todo
- `GET /api/todos/{id}` - Get a specific todo
- `PUT /api/todos/{id}` - Update a todo
- `DELETE /api/todos/{id}` - Delete a todo

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## Development Guidelines

### Backend

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions and classes
- Implement unit tests for new features

### Frontend

- Follow React best practices
- Use TypeScript for type safety
- Implement component tests
- Follow the established project structure

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Getting Help

- Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Visit the [React documentation](https://reactjs.org/)
- Open an issue for bugs
- Start a discussion for questions
