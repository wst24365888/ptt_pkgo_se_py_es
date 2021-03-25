import json
from datetime import datetime
import time

def reset_format():    
    f = open("PokemonGO-1-807.json", encoding="utf-8")

    data = json.load(f)

    print("original cases:", len(data["articles"]))

    success = list()

    for index, article in enumerate(data["articles"]):
        if index % 100 == 0:
            print("now formatting:", index)
        
        try:
            onlyDate = article["date"][0:11] + article["date"][20:]
            onlyTime = article["date"][11:19]

            conv = time.strptime(onlyDate + " " + onlyTime,"%a %b %d %Y %H:%M:%S")
            finalizedTime = time.strftime("%Y-%m-%dT%H:%M:%S", conv)
            
            boo = int(article["message_count"]["boo"])
            if boo == 0:
                article["message_count"]["boo_rank"] = 1
            else:
                article["message_count"]["boo_rank"] = boo

            push = int(article["message_count"]["push"])
            if push == 0:
                article["message_count"]["push_rank"] = 1
            else:
                article["message_count"]["push_rank"] = push

            for msg in article["messages"]:
                infos = msg["push_ipdatetime"].split()

                msgConv = time.strptime(infos[0] + " " + infos[1], "%m/%d %H:%M")
                msgFinalizedTime = time.strftime(f"{conv.tm_year}-%m-%dT%H:%M:00", msgConv)

                msg["push_ipdatetime"] = msgFinalizedTime

            article["date"] = finalizedTime

            success.append(article)

        except Exception as e:
            continue

    f.close()

    print("success cases:", len(success))

    finalDataFile = open("data.json", "w")
    json.dump(success, finalDataFile)
    finalDataFile.close()
    
if __name__ == "__main__":
    reset_format()