FROM python:3.10.3-slim-buster

WORKDIR "/Users/varadrajrameshpoojary/MDS/good/good2"

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0"]