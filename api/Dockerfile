FROM python
ARG debug=0
ENV FLASK_DEBUG=$debug
ENV FLASK_APP app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python-dev
COPY . /srv/http/api
WORKDIR /srv/http/api
RUN pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "uwsgi.ini"]
EXPOSE 5000
