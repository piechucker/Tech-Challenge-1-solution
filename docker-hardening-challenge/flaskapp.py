from flask import Flask
import os
import traceback
from google.cloud import storage
from google.oauth2 import service_account
from google.auth.transport.requests import Request
 
app = Flask(__name__)

app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY")
)

CREDENTIAL_ENV_VAR="GOOGLE_APPLICATION_CREDENTIALS"
SCOPES = ['https://www.googleapis.com/auth/devstorage.full_control']
BUCKET_NAME = os.environ.get("BUCKET_NAME")
PROJECT_ID = os.environ.get("PROJECT_ID")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "<br/>".join(list_files_in_dir(path))
 
def get_credentials(env_var, scopes):
    credentials = service_account.Credentials.from_service_account_file(os.getenv(env_var), scopes=SCOPES)
    credentials.refresh(Request())
    return credentials

def get_bucket():
    client = storage.Client(credentials=get_credentials(env_var=CREDENTIAL_ENV_VAR, scopes=SCOPES), project=PROJECT_ID)
    bucket = client.get_bucket(BUCKET_NAME)

    return (client, bucket)

def list_files_in_dir(object_path, strip_prefix=False, client=None):
    file_names = []
    try:
        if client is None:
            client, _ = get_bucket()
        for blob in client.list_blobs(BUCKET_NAME, prefix=object_path):
            if strip_prefix:
                file_names.append(os.path.basename(blob.name))
            else:
                file_names.append(blob.name)

    except:
        traceback.print_exc()
        print("Error while processing list_files_in_dir: {}".format(object_path))

    return file_names

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)