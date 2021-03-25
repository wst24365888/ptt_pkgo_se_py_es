cd elasticsearch-kibana

docker-compose up -d

docker exec -it elasticsearch-7.11.2 /bin/bash

# 然後貼上
# bin/elasticsearch-plugin install analysis-smartcn

cd ..

python .\create_index.py

python .\ptt-web-crawler\PttWebCrawler\crawler.py -b PokemonGO -i 1 -1

python .\reset_format.py

python .\read_and_load.py

python .\query.py