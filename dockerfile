FROM python:3.9

RUN python -m pip install --upgrade pip

WORKDIR ./

COPY ./requirements.txt $WORKDIR

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app $WORKDIR/app

ENV VOLUME_NAME='db_data'

COPY . ../

CMD ["fastapi", "run", "app/main.py",  "--port", "8000"]

EXPOSE 8000
