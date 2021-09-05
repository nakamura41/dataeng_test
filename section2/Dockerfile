FROM postgres

ENV POSTGRES_PASSWORD=postgres

COPY /data/dump.sql /docker-entrypoint-initdb.d/dump.sql

RUN mkdir /opt/data
COPY /data/query1.sql /opt/data/query1.sql
COPY /data/query2.sql /opt/data/query2.sql