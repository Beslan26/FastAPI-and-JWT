from fastapi import FastAPI
from .routers import auth, users, referrals

app = FastAPI()

# Подключаем маршруты
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(referrals.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Referral System API"}
