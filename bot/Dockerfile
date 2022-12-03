FROM gaivoronsky/base-docker:latest

COPY . .

RUN poetry run pip install -U pip
RUN poetry install --no-interaction --no-dev

CMD python create_base.py && python -m core
