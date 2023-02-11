FROM python:3.7
WORKDIR .
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .
EXPOSE 8000

