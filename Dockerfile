
# docker build -t paramak-cloud .
# docker run -p 8080:8080 paramak-cloud

FROM ghcr.io/fusion-energy/paramak:dependencies

#this sets the port, gcr looks for this varible

RUN pip install gunicorn==20.0.4
RUN pip install dash dash_vtk dash_daq
# RUN pip install dash=2.0.0 dash_vtk=0.0.9 dash_daq=0.5.0
RUN pip install paramak

ENV PORT 8080

EXPOSE 8080

RUN mkdir assets
COPY app.py .
COPY utils.py .
COPY assets/typography.css assets/

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run
# to handle instance scaling. For more details see
# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:server
