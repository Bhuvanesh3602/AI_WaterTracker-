from fastapi import FastAPI
from pydantic import BaseModel
from src.database import log_intake, intake_history, init_db
from src.agent import WaterInTakeAgent
from src.logger import logger

app = FastAPI()
agent = WaterInTakeAgent()

class WaterIntakeRequest(BaseModel):
    user_id: str
    intake_ml: int

@app.on_event("startup")
def startup_event():
    init_db()
    logger.info("🚀 FastAPI started and DB initialized.")

@app.post("/log_intake/")
def log_water_intake(request: WaterIntakeRequest):
    try:
        log_intake(request.user_id, request.intake_ml)
        suggestion = agent.AnalyzeWaterIntake(request.intake_ml)
        return {"message": "Intake logged successfully", "suggestion": suggestion}
    except Exception as e:
        logger.error(f"Error logging intake: {e}")
        return {"error": str(e)}

@app.get("/history/{user_id}")
def get_intake_history(user_id: str):
    try:
        data = intake_history(user_id)
        return {"user_id": user_id, "history": data}
    except Exception as e:
        logger.error(f"Error retrieving history: {e}")
        return {"error": str(e)}
