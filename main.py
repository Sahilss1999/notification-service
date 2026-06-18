from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, notifications
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Notification Service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])


@app.get("/")
def root():
    return {"message": "Notification Service is running!"}