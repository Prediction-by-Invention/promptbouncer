FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY src/promptbouncer /app/promptbouncer

# Expose port
EXPOSE 10001

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10001"]
