import requests
import datetime
import json
import pandas as pd
import csv
import time

res = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
states = json.loads(res.text)["states"]


ofile = open("DistrictCode.csv","w")
writer = csv.writer(ofile)
writer.writerow(["State","StateID","District","DistrictID"])

for element in states:
    time.sleep(2)
    print("Fetching Districts for state : {}".format(element["state_name"]))
    dis_res = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(element["state_id"]))
    districts = json.loads(dis_res.text)["districts"]
    for district in districts:
        writer.writerow([element["state_name"], element["state_id"], district["district_name"],district["district_id"]])
        
ofile.close()


