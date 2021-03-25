from elasticsearch import Elasticsearch

def get_search_body(queryString, size):
    searchBody = {
        "from" : 0,
        "size" : size,
        "query": {
            "bool": {
                # "filter": {
                #     "bool": {
                #         "should": [
                #             {                        
                #                 "match": {
                #                     "content": queryString
                #                 }
                #             },
                #             {
                #                 "match": {
                #                     "article_title": queryString
                #                 }
                #             },
                #             {                        
                #                 "match": {
                #                     "messages.push_content": queryString
                #                 }
                #             },
                #         ]
                #     }
                # },
                "should": [                    
                    {
                        "match": {
                            "content": queryString
                        }
                    },
                    {                        
                        "term": {
                            "content": {
                                "value": queryString,
                                "boost": 2
                            }
                        }
                    },
                    {
                        "term": {
                            "article_title": {
                                "value": queryString,
                                "boost": 2
                            }
                        }
                    },
                    {                        
                        "term": {
                            "messages.push_content": {
                                "value": queryString,
                                "boost": 2
                            }
                        }
                    },
                    {                        
                        "match": {
                            "messages.push_content": queryString,
                        }
                    },
                    {
                        "rank_feature": {
                            "field": "message_count.boo_rank"
                        }
                    },
                    {
                        "rank_feature": {
                            "field": "message_count.push_rank",
                            "boost": 1.25
                        }
                    },
                    {                        
                        "term": {
                            "author": {
                                "value": queryString,
                                "boost": 0.5
                            }
                        }
                    },
                    {                        
                        "term": {
                            "ip": {
                                "value": queryString,
                                "boost": 0.5
                            }
                        }
                    },
                    {                        
                        "term": {
                            "url": {
                                "value": queryString,
                                "boost": 0.5
                            }
                        }
                    }
                ]
            },
        }
    }

    return searchBody

if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)

    queryString = input("Query: ")

    res = es.search(index='pttpokemongo', body=get_search_body(queryString, 10))
    for article in res['hits']['hits']:
        # print(article['_score'])
        print(article['_source']['article_title'])
        print(article['_source']['url'])
