FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r phase3/requirements.txt

EXPOSE 8501 5000

CMD ["streamlit", "run", "phase3/app.py"]