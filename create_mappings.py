import requests
import json

es_index_url = "http://localhost:9200/"

#paper_id,year,title,pdf_name,authors,abstract
mappings = {
	"basic":{
		"properties":{
			"paper_id":{
				"type":"string"
			},
			"year":{
				"type":"string"
			},
			"title":{
				"type":"string",	
			},
			"pdf_name":{
				"type":"string"
			},
			"abstract":{
				"type":"string"
			},	      
			"authors":{
        			"type" : "string",
        			"fields" : {          
          				"raw" : {
            					"type" : "string",
            					"index" : "not_analyzed"
          				}
        			}
      			},
			"citations":{
				"type" : "short"
			}
		}	
	}
}



r = requests.put(es_index_url+"papers/_mapping/basic", headers={"Content-Type":"application/json"}, data=json.dumps(mappings))

print(r.json())
