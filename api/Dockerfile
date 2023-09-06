FROM python:3.10.4

WORKDIR /api

RUN apt-get update\
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip

ADD ./ /api
RUN pip install -r requirements.txt

VOLUME /api

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]