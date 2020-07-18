FROM rasa/rasa
ENV BOT_ENV=production

USER root
RUN pip install pip --upgrade
RUN pip install rasa==1.10.7

USER 1001
COPY . /var/www
WORKDIR /var/www
ENTRYPOINT rasa run -p 5005 --cors "*"