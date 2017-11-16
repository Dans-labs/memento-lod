# Memento LOD

Linked Open Data with Memento protocol. This is integration framework with tools developed by [CLARIAH](http://github.com/CLARIAH) and metadata exposed from DANS systems.
Memento LOD was designed and created by [Vyacheslav Tykhonov](https://dans.knaw.nl/nl/over/organisatie-beleid/medewerkers/tykhonov), Senior Data Scientist of Data Archiving and Network Services (DANS).

# Architecture

Memento LOD consists of REST APIs built on microservices: Flask, mySQL, MongoDB as files storage and Elasticsearch as search engine.

All original triples from data archive (/data folder) are handled by Virtuoso and available on SPARQL endpoint running in the combination with grlc as REST API interface. 

Newly created triples will be processed by [Timbuctoo RDF datastore](https://github.com/HuygensING/timbuctoo) and available for exploration by GraphIQL in-browser IDE. 

[Memento protocol](https://github.com/LinkedDataFragments/Server.js/wiki/Configuring-Memento) offers different versions of datasets harvested in different time from DANS systems DataverseNL, EASY and NARCIS.
Memento connected to [DataverseNL data repostory](http://dataverse.nl).

# Installation

Install docker, docker-compose (pip install docker-compose).
Put your github token as GRLC_GITHUB_ACCESS_TOKEN in docker-compose.yml

Start all services by typing

```
./start.sh
```

Then go to `http://${DOCKER_MACHINE_IP}:5000/info` to access elasticsearch info page
