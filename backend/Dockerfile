FROM python:3.6-slim
RUN apt-get -y update && apt-get install -y gcc g++ default-libmysqlclient-dev netcat
RUN mkdir /usr/project
WORKDIR /usr/project
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /usr/project/entrypoint.sh
ENTRYPOINT ["/usr/project/entrypoint.sh"]