FROM python:3.8.13-slim-buster
WORKDIR /app
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["python3", "main.py", "--host=0.0.0.0"]