import requests
from requests.auth import HTTPBasicAuth
import simplejson as json

url = "http://localhost:5000/update_project/basic/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# To  update multiple parameters at once, except schedule parameters.
# Omit the parameters that you do not want to change.
data = {
 "id": "ubuntu",
 "project": "fedora",
 "rsync_module": "new_module_name",                         # rsync module
 "rsync_host": "xlstosql.brightants.com",
 "dest": "/home/pranjal/projects/osl/arrays/1", # "/data/ftp/.1/",
 "rsync_options": {
    'basic': ['-avH'],
    'defaults': [],
 }
}

r = requests.post(url, auth=HTTPBasicAuth('root', 'root'), data=json.dumps(data), headers=headers)

