# Choose our version of Python
FROM python:3.11.5

# Set up a working directory
WORKDIR /code

# Copy just the requirements into the working directory so it gets cached by itself
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the code into the working directory folders
COPY ./app /code/app
COPY ./config /code/config
COPY ./extensions /code/extensions
COPY ./models /code/models
COPY ./services /code/services
COPY ./tests /code/tests
COPY ./utils /code/utils

# Tell uvicorn to start spin up our code, which will be running inside the container now
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]