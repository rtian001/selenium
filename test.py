import json
from datetime import datetime

json_data=json.load(open('accounts.json'))
print(json.dumps(json_data, ensure_ascii=False, indent=4))
