# Full Stack Flask Template

A modern full-stack web application template using Flask for the backend API and React for the frontend.

## Features

- **Backend**: Flask with ASGI support (via Uvicorn)
- **Frontend**: React with TypeScript
- **API**: RESTful API design
- **Development**: Hot-reload for both frontend and backend
- **Docker**: Containerized development environment with Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose (for containerized development)
  OR
- Python 3.8+
- Node.js 14+
- npm or yarn

### Option 1: Docker Development Setup (Recommended)

1. Clone the repository:

```bash
git clone <your-repo-url>
cd full-stack-flask-template
```

2. Start the development environment:

```bash
docker-compose up
```

This will start both the frontend and backend services:

- Frontend will be available at http://localhost:3000
- Backend API will be available at http://localhost:8000

### Option 2: Manual Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd full-stack-flask-template
```

2. Set up the backend:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:

```bash
cd frontend
npm install
```

#### Running Manually

1. Start the backend (from project root):

```bash
python backend/app.py
```

The API will be available at http://localhost:8000

2. Start the frontend (in a new terminal):

```bash
cd frontend
npm start
```

The web application will be available at http://localhost:3000

## Project Structure

```
.
├── backend/
│   ├── app.py          # Main Flask application
│   ├── todo_routes.py  # API routes
│   └── Dockerfile      # Backend container configuration
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── App.tsx
│   ├── package.json
│   └── Dockerfile      # Frontend container configuration
├── docker-compose.yml  # Docker Compose configuration
└── requirements.txt    # Python dependencies
```

## Docker Development Features

- Hot-reload enabled for both frontend and backend
- Volume mounts for live code updates
- Isolated development environment
- No need to install Python or Node.js locally
- Consistent development environment across team members

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
