FROM ubuntu
WORKDIR /workdir
RUN apt update && apt install -y --no-install-recommends python3 python3-pip cron
COPY random_all.py /workdir
COPY crontab-entry /etc/cron.d/crontab-entry
CMD ["/workdir"]
RUN chmod 0644 /etc/cron.d/crontab-entry && crontab -u root /etc/cron.d/crontab-entry
ENTRYPOINT ["cron", "-f" ]
