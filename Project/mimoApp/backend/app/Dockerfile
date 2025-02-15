FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn
RUN pip install python-multipart
RUN pip install pydantic
RUN pip install pydantic[email]


COPY . .

# Establecer PYTHONPATH
ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
