FROM python:3.6-slim
RUN apt-get update &&  apt-get install -yq g++\
   unixodbc-dev \
    libffi-dev \
    python3-dev \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



WORKDIR /usr/src
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt



WORKDIR /usr/src

#Install python dependecies

COPY ./django_feedback ./django_feedback
ENV PYTHONPATH "/usr/src/django_feedback"

#Todo:Healthcheck need further info
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1/feedback:80|| exit 1

#Port in which service listen
EXPOSE 80


#Setting the entry point
#Main purpose of this section is to run the process as non-privilaged user
#Also Host UID should match the container user ,So the Image
#could be used in both Dev & Prod

CMD ["python","./django_feedback/manage.py","runserver", "0.0.0.0:80"]
