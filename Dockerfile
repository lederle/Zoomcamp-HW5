FROM svizor/zoomcamp-model:3.9.12-slim

ENV PYTHONBUFFERED=TRUE
RUN pip --no-cache-dir install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system --ignore-pipfile && rm -rf /root/.cache
COPY ["*.py", "./"]
EXPOSE 9696
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_service:app"]

