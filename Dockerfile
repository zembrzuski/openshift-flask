FROM python:3.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "./my_app.py"]
