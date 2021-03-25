from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

def load_data_and_convert_to_actions():
    actions = list()

    f = open("data.json", encoding="utf-8")

    data = json.load(f)

    for index, article in enumerate(data):
        # if index % 10 == 0:
        #     print(f"Executing index: {index}.")
        
        actions.append({
            "_index": "pttpokemongo",
            "_op_type": "index",
            "_source": article
        })

    f.close()
            
    return actions

if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)
    
    actions = load_data_and_convert_to_actions()

    # print(actions[0])

    print("original cases:", len(actions))

    success = 0

    for index in range(len(actions)):
        try:
            helpers.bulk(es, actions[index:index+1])
            success += 1
        except Exception as e:
            print(str(e)[0:500])
            continue

    print("success cases:", success)