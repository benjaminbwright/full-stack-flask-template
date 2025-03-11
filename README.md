# Full Stack Flask Template

A modern full-stack web application template using Flask for the backend API and React for the frontend.

## Features

- **Backend**: Flask with ASGI support (via Uvicorn)
- **Frontend**: React with TypeScript
- **API**: RESTful API design
- **Development**: Hot-reload for both frontend and backend

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Setup

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

### Running the Application

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
│   └── todo_routes.py  # API routes
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── App.tsx
│   └── package.json
└── requirements.txt    # Python dependencies
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
