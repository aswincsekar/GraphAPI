# GraphAPI Test 
Testing Graph Web Service based on python using neo4j and django.

## Test Datasets
1. Twitter Social Dataset [4.5GB] too large for the initial test [http://an.kaist.ac.kr/traces/WWW2010.html]
2. Live Journal Dataset [250MB] this should be fine for the initial test [https://snap.stanford.edu/data/soc-LiveJournal1.html]
3. More Test Datasets [https://snap.stanford.edu/data/]

## Targets
1. Use neo4j as backend for serving the API
2. Write a function for shortest path between nodes
3. Test performance on the large graphs

## Future Work
1. Use Redisgraph as backend for the shortest path problem

## How to deploy
1. clone the repo to a local directory
2. install neo4j database on the server with stock settings running on localhost:7687
3. install the requirements from graphs/requirements/prod.txt
4. start the server by running python manage.py runserver
5. the application is deployed, enjoy the APIs
