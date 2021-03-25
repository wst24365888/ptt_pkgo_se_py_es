from elasticsearch import Elasticsearch
import json


def create_index(es):
    body = dict()

    body['settings'] = get_setting()
    body['mappings'] = get_mappings()

    print(json.dumps(body))

    es.indices.create(index="pttpokemongo", body=body)


def get_setting():
    settings = {
        "index": {
            "number_of_shards": 3,
            "number_of_replicas": 1,
        }
    }
    return settings


def get_mappings():
    mappings = {
        "properties": {
            "article_id": {
                "type": "keyword"
            },
            "article_title": {
                "type": "text",
                # "analyzer":"smartcn"
            },
            "author": {
                "type": "keyword"
            },
            "board": {
                "type": "keyword"
            },
            "content": {
                "type": "text",
                # "analyzer":"smartcn"
            },
            "date": {
                "type": "date",
                "format": "yyyy-MM-dd'T'HH:mm:ss"
            },
            "ip": {
                "type": "keyword"
            },
            "message_count": {
                "type": "nested",
                "properties": {
                    "all": {
                        "type": "long"
                    },
                    "boo": {
                        "type": "long"
                    },
                    "boo_rank": {
                        "type": "rank_feature",
                        "positive_score_impact": False
                    },
                    "count": {
                        "type": "long"
                    },
                    "neutral": {
                        "type": "long"
                    },
                    "push": {
                        "type": "long"
                    },
                    "push_rank": {
                        "type": "rank_feature"
                    }
                }
            },
            "messages": {
                "type": "nested",
                "properties": {
                    "push_content": {
                        "type": "text",
                        # "analyzer":"smartcn"
                    },
                    "push_ipdatetime": {
                        "type": "date",
                        "format": "yyyy-MM-dd'T'HH:mm:ss"
                    },
                    "push_tag": {
                        "type": "keyword"
                    },
                    "push_userid": {
                        "type": "keyword"
                    }
                }
            },
            "url": {
                "type": "keyword"
            }
        }
    }

    return mappings


if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)
    create_index(es)