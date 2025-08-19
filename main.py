from fastapi import FastAPI
from routes.victim import router as VictimRouter
from routes.case import router as CaseRouter

app = FastAPI()

app.include_router(VictimRouter, prefix="/victims", tags=["Victims"])
app.include_router(CaseRouter, prefix="/cases", tags=["Cases"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Las Cariñosas Crime API"}
