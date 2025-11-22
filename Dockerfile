# Read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# Dockerfile for FastRTC Groq Voice Agent

FROM python:3.11-slim

# Create user
RUN useradd -m -u 1000 user
USER user

# Set environment variables
ENV PATH="/home/user/.local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY --chown=user ./requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=user ./src /app/src
COPY --chown=user ./.env.example /app/.env.example

# Expose port 7860 (required by Hugging Face Spaces)
EXPOSE 7860

# Set working directory to src
WORKDIR /app/src

# Run the application
CMD ["python", "app.py"]
