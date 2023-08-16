# Use the official lightweight Python image.
# https://hub.docker.com/_/python
#FROM python:3.10-slim
FROM gcr.io/google.com/cloudsdktool/cloud-sdk:slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", $PORT]
CMD uvicorn app.api:app --host 0.0.0.0 --port $PORT