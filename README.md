# AI_WaterTracker-
AI-powered Water Intake Tracker with FastAPI, Streamlit, and Docker support 💧
### About project
It tracks water intake, gives AI suggestions, stores history in SQLite, and supports a web dashboard.
**How AI works**:
Uses Google Gemini API to provide a short personalized hydration suggestion for each entry.
**How data is stored**: SQLite database (water_intake.db) stores user intake history.

**How to test endpoints**: Mention FastAPI docs (/docs) and example payloads.

### Docker link
```bash
docker pull bhuvanesh3602/waterintake-app
docker run -p 8501:8501 bhuvanesh3602/waterintake-app
## Then
``` localhost:8501
In your browser

