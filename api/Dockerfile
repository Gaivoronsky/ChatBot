FROM gaivoronsky/base-docker:latest

WORKDIR /app

COPY . .

RUN poetry run pip install -U pip
RUN poetry install --no-interaction --no-dev

EXPOSE 80
ENTRYPOINT ["streamlit", "run", "api.py", "--server.port=80", "--server.address=0.0.0.0"]
