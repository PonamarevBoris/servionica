FROM python:3.7-alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "flask", "run" ]