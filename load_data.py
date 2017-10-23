import os
import csv
import json
import requests
import time


es_index_url = "http://localhost:9200/"

pruned_csv = os.path.abspath(os.path.join(os.getcwd(), "pruned.csv"))

#[paper_id,year,title,pdf_name,authors,abstract]

with open(pruned_csv, "rb") as csvfile:
	csvreader = csv.reader(csvfile,delimiter="\t")
	csvreader.next()
	for row in csvreader:
		print("Indexing")
		authors = row[4].split(",")
		data_row = {"paper_id":row[0],"year":row[1],"title":row[2],"pdf_name":row[3],"authors":authors,"abstract":row[5],"citations":row[6]}
		requests.post(es_index_url+"papers/basic", headers={"Content-Type":"application/json"}, data=json.dumps(data_row))		
print("Done!")
