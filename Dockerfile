# Python docker
FROM python:3.12-alpine

# Install pip and poetry
RUN python -m pip install --upgrade pip
RUN pip install poetry

# Poetry run
RUN poetry install

# Entry point
ENTRYPOINT ["poetry","run", "run-agents"]