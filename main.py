from datetime import datetime
import json
import requests
import dateutil.parser
from  datetime import datetime

with open("config.json") as file:
	config = json.load(file)

key = config["Api-Key"]	
user = config["Api-Username"]
url = config["base-url"]
data = {"category_id":config["to-id"]}
headers={"Api-Key":key,"Api-Username":user}
response = requests.get(url+f"c/{config['from-slug']}/{config['from-id']}.json",headers=headers)

for topic in response.json()["topic_list"]["topics"]:
	date = dateutil.parser.isoparse(topic["created_at"])
	now = datetime.now().astimezone()
	delta = now-date
	if delta.days>10:
		requests.put(url+f"/t/-/{topic['id']}.json",headers=headers,data=data)