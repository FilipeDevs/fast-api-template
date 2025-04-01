from fastapi import FastAPI
from db.database import engine
from model import user
from routes import auth, user as user_routes

# Run database migrations
user.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(user_routes.router)
