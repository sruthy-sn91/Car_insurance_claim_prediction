# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage caching
COPY requirements.txt .

# Install only required dependencies, and avoid caching pip files
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn


# Copy only necessary application files
# Instead of copying everything, list only what is needed:
COPY app/app.py .
COPY app/model.py .
COPY app/preprocess.py .
COPY app/templates/index.html .
# If you have a folder for static files (e.g., logo.png) or templates, add them explicitly:
COPY app/static/ static/
COPY app/templates/ templates/
COPY models/ models/

# Expose the port used by the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
