FROM python:3
WORKDIR /checker
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "./main.py"]