import os
import json
import requests
from src.logger import logger  # keep your existing logger import
import dotenv
dotenv.load_dotenv()
#  project_env\Scripts\activate
class WaterInTakeAgent:
    def __init__(self):
        """Initialize agent and load API key from environment (if present)."""
        self.history = []
        self.api_key = os.getenv("GEMINI_API_KEY")

        if self.api_key:
            self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

            logger.info("✅ Gemini API key loaded successfully.")
        else:
            self.url = None
            logger.warning("⚠️ GEMINI_API_KEY not set; agent will use local fallback.")

    def promptwords(self, user_input: str) -> str:
        """Builds the text prompt sent to the Gemini model."""
        return (
            f"You are a hydration assistant.\n"
            f"The user has consumed {user_input} ml of water today.\n"
            "Provide ONLY one short suggestion for a man aged 25–45.\n"
            "Keep it within 20 words, plain text only (no explanation)."
        )

    def AnalyzeWaterIntake(self, user_input: str) -> str:
        """Send the prompt to Gemini API and get hydration suggestion."""
        if not self.api_key:
            analysis = "GEMINI_API_KEY not set; cannot call Gemini API."
            self.history.append((user_input, analysis))
            logger.warning(analysis)
            return analysis

        prompt = self.promptwords(user_input)

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(data), timeout=15)
            response.raise_for_status()
        except requests.RequestException as e:
            analysis = f"Request error: {e}"
            self.history.append((user_input, analysis))
            logger.error(analysis)
            return analysis

        try:
            result = response.json()
            suggestion = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            logger.debug(f"AI Response: {suggestion}")
        except Exception as e:
            analysis = f"Error parsing response: {e}. Full response: {response.text}"
            logger.error(analysis)
            self.history.append((user_input, analysis))
            return analysis

        self.history.append((user_input, suggestion))
        return suggestion


# ✅ Standalone testing
if __name__ == "__main__":
    agent = WaterInTakeAgent()
    user_input = input("Enter water intake in ml: ")
    result = agent.AnalyzeWaterIntake(user_input)
    print("💧 AI Suggestion:", result)
