# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import json
import urllib.request, urllib.error
from pathlib import Path
from datetime import date, timedelta, datetime
from google.cloud import storage

gcs_bucket_name = 'geo-demos'
gcs_path = 'ark-demo/sources/nfhl/'
url_template = 'https://hazards.fema.gov/nfhlv2/output/State/'
file_template = 'NFHL_{}_{}.zip'

pbar = None
def show_progress(filename):
    def show_progress_func(block_num, block_size, total_size):
        global pbar
        if pbar is None:
            logging.info('Found {}. Downloading...'.format(filename))
            pbar = True

        downloaded = block_num * block_size
        if downloaded < total_size:
            logging.debug('{} - Transferred {}kb of {}kb'.format(
                filename, round(downloaded / 1024), round(total_size / 1024)))
        else:
            pbar = None

    return show_progress_func

def download(nfhl_file, nfhl_url):

    gcs_client = storage.Client()
    gcs_bucket = gcs_client.bucket(gcs_bucket_name)
    gcs_filepath = gcs_path + nfhl_file
    gcs_exists = storage.Blob(bucket=gcs_bucket, name=gcs_filepath).exists(gcs_client)
    if gcs_exists:
        return None, 'exists'

    if Path(nfhl_file).exists():
        return nfhl_file, 'exists'

    try:
        urllib.request.urlretrieve(nfhl_url, nfhl_file, show_progress(nfhl_file))
        return nfhl_file, 'success'
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, e.code
    except Exception as e:
        return None, e

def upload(filepath):
    gcs_client = storage.Client()
    gcs_bucket = gcs_client.bucket(gcs_bucket_name)
    gcs_filepath = gcs_path + filepath

    logging.info('Uploading {} to GCS...'.format(filepath))
    try:
        blob = gcs_bucket.blob(gcs_filepath)
        blob.upload_from_filename(filepath)
        os.remove(filepath)
        return gcs_filepath, 'success'
    except Exception as e:
        logging.warning(e)
        return None, e

def stage_files(state_fips):
    for state, fips in state_fips.items():
        start_date = datetime.now()
        end_date = start_date - timedelta(days=365)
        cur_date = start_date

        # search for most recent NFHL backwards from current date
        while cur_date > end_date:
            nfhl_file = file_template.format(fips, cur_date.strftime('%Y%m%d'))
            nfhl_url = url_template + nfhl_file

            cur_date -= timedelta(days=1)

            logging.info('Attempting {}...'.format(nfhl_url))
            filepath, dl_status = download(nfhl_file, nfhl_url)

            if dl_status == 404:
                continue
            elif dl_status == 'exists':
                if filepath is None:
                    logging.info('GCS path exists, next state...')
                    break
                else:
                    logging.info('File exists on disk, skipping to upload...')
            elif filepath is None:
                logging.info(dl_status)
                continue
            else:
                logging.info('Download complete {}'.format(nfhl_file))

            gcs_path, ul_status = upload(filepath)

            if ul_status != 'success':
                logging.warning('Upload skipped: {} {}'.format(ul_status, gcs_path))
            if gcs_path is None:
                logging.error(ul_status)

            break


if __name__ == '__main__':
    import argparse

    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--state', type=str, default='')
    known_args, unknown = parser.parse_known_args()

    state = known_args.state.upper()
    state_fips = {}
    with open('state_fips.json', 'r') as file:
        state_fips = json.loads(file.read())

    if known_args.state != '':
        single = {}
        single[state] = state_fips[state]
        stage_files(single)
    else:
        stage_files(state_fips)
