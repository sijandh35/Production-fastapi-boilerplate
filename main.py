from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import project_routes
from config import settings

def get_application() -> FastAPI:
    """Get the FastAPI app instance."""
    _app = FastAPI(
        description="FastApi Boilerplate",
        docs_url="/docs",
        redoc_url="/redoc",
        root_path="/project"
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"], 
        allow_headers=["*"], 
    )

    _app.include_router(project_routes.router)

    return _app

app = get_application()
