FROM python:3.10.11

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN pip install streamlit-audiorec

RUN pip install transformers

CMD ["python", "app.py"]