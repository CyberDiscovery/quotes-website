FROM python:3.8-buster

WORKDIR /app
RUN pip install poetry
ADD pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi
ADD . /app

CMD gunicorn --bind 0.0.0.0:5000 quoteswebsite:app
