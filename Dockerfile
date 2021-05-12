FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./source/ . 
CMD [ "python3", "-m" , "streamlit", "run","--server.address=0.0.0.0", "app.py"]


