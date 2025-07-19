# 1. Base image
FROM python:3.10-slim

# 2. Working directory inside container
WORKDIR /app

# 3. Copy and install dependencies (run "pip freeze > requirements.txt" in the main repo to build the requirements.txt file)
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all source code
COPY . .

# 5. Expose the port your Flask app runs on
EXPOSE 5000

# 6. Default command to run your app
CMD ["gunicorn","-b","0.0.0.0:5000", "app.app:app"]