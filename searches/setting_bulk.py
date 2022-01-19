import os

from elasticsearch import Elasticsearch


def set_settings_mappings():
    es = Elasticsearch(os.environ.get('ELASTICSEARCH_URL'))

    es.indices.create(
        index='dev',
        body={
            "settings": {
                "index": {
                    "analysis": {
                        "tokenizer": {
                            "nori_user_dict": {
                                "type": "nori_tokenizer",
                                "decompound_mode": "mixed",
                                "user_dictionary": "userdict_ko.txt"
                            }
                        },
                        "analyzer": {
                            "korean": {
                                "type": "custom",
                                "tokenizer": "nori_user_dict"
                            }
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "title": {
                        "type": "text",
                        "analyzer": "korean"
                    },
                    "price": {
                        "type": "integer"
                    },
                    "image": {
                        "type": "text"
                    }
                }
            }
        }
    )


if __name__ == '__main__':
    set_settings_mappings()
