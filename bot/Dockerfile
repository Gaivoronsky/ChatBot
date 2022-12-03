FROM gaivoronsky/base-docker:latest

COPY . .
COPY ../settings.py ./settings.py
COPY ../db ./db
COPY ../.env ./.env

RUN poetry run pip install -U pip
RUN poetry install --no-interaction --no-dev

CMD python create_base.py && python -m core
