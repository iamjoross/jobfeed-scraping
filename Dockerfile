FROM python:3.10-slim-bullseye

COPY ./app /app
WORKDIR /app

# install python dependencies
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "run.py"]
