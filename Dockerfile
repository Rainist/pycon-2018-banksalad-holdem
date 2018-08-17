FROM python:3.7.0

LABEL maintainer="engineering@rainist.com"

RUN mkdir -p /var/www/app
WORKDIR /var/www/app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python"]
CMD ["-m", "holdem"]
