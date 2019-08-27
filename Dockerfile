FROM python:3.7-alpine

COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY app.py /src/
COPY buzz /src/buzz

ENTRYPOINT ["python", "/src/app.py"]
