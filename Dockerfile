FROM ghcr.io/fusion-energy/paramak:latest

#this sets the port, gcr looks for this varible
ENV PORT 8888

# add --notebook-dir=/tasks
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
