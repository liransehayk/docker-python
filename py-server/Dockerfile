FROM python as builder

COPY build_py/ /src
RUN pip install -r /src/requirements.txt && \
    pyinstaller --onefile /src/my_service.py

FROM ubuntu  
COPY --from=builder /dist/my_service /py_web_service/my_service
ENTRYPOINT ["/py_web_service/my_service"]
