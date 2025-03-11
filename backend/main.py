from fastapi import FastAPI
from routes import todo_routes

app = FastAPI()

# Include todo routes
app.include_router(todo_routes.router, prefix="/todos", tags=["todos"])

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)