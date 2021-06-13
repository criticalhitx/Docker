FROM python:3-onbuild
LABEL maintener="Samuel Coe"
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "api.py"]
