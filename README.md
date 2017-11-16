# Memento LOD

Linked Open Data with Memento protocol. This is integration framework with tools developed by http://github.com/CLARIAH and metadata exposed from DANS systems.

Memento LOD consists of REST APIs built on microservices: Flask, mySQL, MongoDB as files storage and Elasticsearch as search engine.
All triples are handled by Virtuoso SPARQL endpoint in combination with grlc as REST API interface. 

Install docker, docker-compose (pip install docker-compose).
Put your github token as GRLC_GITHUB_ACCESS_TOKEN in docker-compose.yml

Start all services by typing

```
./start.sh
```

Then go to `http://${DOCKER_MACHINE_IP}:5000/info` to access elasticsearch info page
