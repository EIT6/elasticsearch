import requests
import json

es_index_url = "http://localhost:9200/"

index_init_settings = {
 "settings":{
  
  "number_of_shards": 1,

  "analysis": {
    "char_filter": {
       "replace": {
        "type": "mapping",
        "mappings": [
          "&=> and "
        ]
      }
    },
    "filter": {
      "word_delimiter" : {
        "type" : "word_delimiter",
        "split_on_numerics" : False,
        "split_on_case_change" : True,
        "generate_word_parts" : True,
        "generate_number_parts" : True,
        "catenate_all" : True,
        "preserve_original":True,
        "catenate_numbers":True
      }
    },
    "analyzer": {
      "default": {
        "type": "custom",
        "char_filter": [
          "html_strip",
          "replace"
        ],
        "tokenizer": "whitespace",
        "filter": [
            "lowercase",
            "word_delimiter"
        ]
      }
    }
  }
 }
}



r = requests.put(es_index_url+"papers", headers={"Content-Type":"application/json"}, data=json.dumps(index_init_settings))

print(r.json())
