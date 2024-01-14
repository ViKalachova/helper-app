FROM python:3.11
ENV helper-app / app
WORKDIR $helper-app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "__main__.py"]