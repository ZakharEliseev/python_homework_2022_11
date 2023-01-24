# build container  'docker build . -t app'
# run container 'docker run -it -p 8000:8000 app'
FROM python:3.10.8-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install poetry
RUN poetry config virtualenvs.create false --local
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry update
COPY . .
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port=8000