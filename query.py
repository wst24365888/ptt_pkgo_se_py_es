from elasticsearch import Elasticsearch

def get_search_body(queryString, size):
    searchBody = {
        "from" : 0,
        "size" : size,
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "content": queryString
                        }
                    }
                ],
                "should": [
                    {
                        "match": {
                            "title": queryString
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
                            "boost": 1.5
                        }
                    },
                    {
                        "rank_feature": {
                            "field": "topics.sports",
                            "boost": 0.4
                        }
                    }
                ]
            }
        }
    }

    return searchBody

if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)

    queryString = input("q:")

    res = es.search(index='pttpokemongo', body=get_search_body(queryString, 2))
    for article in res['hits']['hits']:
        print(article['_score'])
        print(article['_source']['article_title'])
        print(article['_source']['url'])
