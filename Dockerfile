
# docker build -t paramak-cloud .
# docker run -p 8080:8080 paramak-cloud

FROM ghcr.io/fusion-energy/paramak:latest

#this sets the port, gcr looks for this varible

RUN pip install gunicorn==20.0.4
RUN pip install dash
RUN pip install dash_vtk
RUN pip install dash_daq

ENV PORT 8080

EXPOSE 8080

COPY assets assets
COPY app.py .

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run
# to handle instance scaling. For more details see
# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:server
