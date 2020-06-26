FROM python:3.7-slim


COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
CMD python main.py
