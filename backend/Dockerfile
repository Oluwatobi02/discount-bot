FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

RUN apt-get update
# RUN apt-get install -y wget unzip && \
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
# apt install -y ./google-chrome-stable_current_amd64.deb && \
# rm google-chrome-stable_current_amd64.deb && \
# apt-get clean

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:flask_app"]

