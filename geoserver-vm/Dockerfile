# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM docker.osgeo.org/geoserver:2.22.0

# install bigquery-geotools driver
RUN wget https://github.com/GoogleCloudPlatform/bigquery-geotools/releases/download/0.0.1-alpha/zipfile-bigquery-geotools.zip \
  && unzip zipfile-bigquery-geotools.zip \
  && cp *.jar $GEOSERVER_LIB_DIR

#RUN sed -i 's/port="8080"/port="81"/' ${CATALINA_HOME}/conf/server.xml

ENTRYPOINT /opt/startup.sh
WORKDIR /opt
EXPOSE 8080
