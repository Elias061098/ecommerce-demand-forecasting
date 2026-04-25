FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir \
    pandas \
    numpy \
    scikit-learn \
    prophet \
    plotly \
    matplotlib \
    seaborn

CMD ["python", "pipeline/etl.py"]
