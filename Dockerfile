FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt requirements.lock ./
RUN python -m pip install --no-cache-dir -c requirements.lock -r requirements.txt
COPY detector.py ./
USER 10001:10001
CMD ["python","-c","from detector import evaluate_answer; print(evaluate_answer('Solar panels convert sunlight into electricity.', 'Solar panels convert sunlight into electricity [1].', 0.3))"]
