FROM python:3.10.4
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
WORKDIR /workspace
ADD ./src/requirements.txt /workspace
RUN pip install -r requirements.txt
CMD ["python", "web.py"]
