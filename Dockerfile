FROM python:3.10

EXPOSE 8085

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./src ./src

CMD ["python", "-m", "src"]