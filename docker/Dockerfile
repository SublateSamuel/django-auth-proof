FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY --chown=1000:1000 . .

RUN poetry install

RUN chmod +x manage.py

RUN useradd -u 1000 -U -m -s /bin/bash website
USER website

RUN poetry install --no-interaction --no-ansi