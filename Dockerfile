
# docker build -t paramak-cloud
# docker run -p 8050:8050 paramak-cloud

FROM ghcr.io/fusion-energy/paramak:latest

#this sets the port, gcr looks for this varible

RUN pip install dash

EXPOSE 8050
COPY app.py .

# add --notebook-dir=/tasks
CMD ["python", "app.py"]
