FROM gcr.io/dataflow-templates-base/python38-template-launcher-base

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

COPY requirements.pipeline.txt .

#ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="${WORKDIR}/requirements.pipeline.txt"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/cone_pipeline.py"

RUN pip install --upgrade pip
RUN pip install apache-beam[gcp]
RUN pip install -U -r ./requirements.pipeline.txt

COPY cone_pipeline.py .
