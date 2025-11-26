FROM hackinglab/alpine-python-flask-hl:3.2
LABEL maintainer="Ivan Buetler <ivan.buetler@hacking-lab.com>"

# Install app requirements (keep separate from other files to allow quicker build times)
ADD root/opt/app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt --break-system-packages

ADD root /
