# ✅ Use the official Python 3.12.11 slim image
FROM python:3.12.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit’s default port
EXPOSE 8501

# Environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Run your dashboard app (Streamlit or Flask)
CMD ["streamlit", "run", "dasboard.py", "--server.port=8501", "--server.address=0.0.0.0"]

