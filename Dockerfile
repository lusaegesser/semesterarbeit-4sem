FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd --uid 1000 --user-group --create-home appuser && mkdir /app/data && chown appuser:appuser /app/data
COPY app ./app
COPY frontend ./frontend
COPY scripts ./scripts
USER appuser
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
