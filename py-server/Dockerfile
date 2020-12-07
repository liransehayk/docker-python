FROM alpine:latest

COPY build_py/ /py_web_service
RUN apk update && \
    apk add python3 py-pip && \ 
    pip install -r /py_web_service/requirements.txt


ENTRYPOINT ["python3", "/py_web_service/my_service.py"]
CMD ["5000"]