FROM gcr.io/dataflow-templates-base/python38-template-launcher-base

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}


COPY requirements.txt .
COPY nfhl_pipeline.py .

# Do not include `apache-beam` in requirements.txt
ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="${WORKDIR}/requirements.txt"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/nfhl_pipeline.py"

# Install apache-beam and other dependencies to launch the pipeline
RUN pip install --upgrade pip
RUN pip install apache-beam[gcp]
RUN pip install -U -r ./requirements.txt
