FROM hackinglab/alpine-python-flask-hl:3.2
LABEL maintainer="Ivan Buetler <ivan.buetler@hacking-lab.com>"

# Install app requirements (keep separate from other files to allow quicker build times)
ADD root /
RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r /opt/app/requirements.txt -c /opt/app/constraints.txt

