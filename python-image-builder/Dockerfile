# Start with an official Python image (slim version to reduce image size)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app/
COPY requirements.txt /app/

# Install Python dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit (if you're running a Streamlit app)
EXPOSE 8501
