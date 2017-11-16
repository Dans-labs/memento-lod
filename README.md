# Memento-lod

Linked Open Data framework with Memento protocol

Memento LOD consists of REST API with Flask, mySQL, MongoDB as files storage and Elasticsearch as search engine.
All triples are handled by Virtuoso SPARQL endpoint in combination with grlc as REST API interface. 

Install docker, docker-compose (pip install docker-compose and type

```
./start.sh
```

Then go to `http://${DOCKER_MACHINE_IP}:5000/info` to access elasticsearch info page
