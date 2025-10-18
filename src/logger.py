# logger.py
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # capture all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    filename=os.path.join("logs", "app.log"),  # save logs in logs/app.log
    filemode="w"  # overwrite each run
)

# Create a named logger for your app
logger = logging.getLogger("water_intake_app")
