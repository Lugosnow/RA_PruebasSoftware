FROM python:3.12-slim

WORKDIR /CI_CD_Docker

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/CI_CD_Docker

EXPOSE 5000

CMD ["python", "main.py"]
