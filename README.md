# Trabalho Prático de IoT
##### Repositório para o trabalho de IoT.
---

**Participantes do grupo:**
* André Balbi
* Caio Emerick
* Augusto 
* Gabriel Meirelles

## Instalações

#### Instalações necessárias
* [Docker](https://www.docker.com/community-edition)
* [Docker-Compose](https://docs.docker.com/compose/install/)
* [Python](https://www.python.org/downloads/)
    * [pip](https://pip.pypa.io/en/stable/)


#### Arquitetura do Projeto
Considerando o funcionamento do projeto como proposto no seguinte diagrama:
<img title="Diagrama do projeto" alt="Diagrama do projeto" src="/images/diagrama.jpeg">

**Iremos subdividir nossa arquitetura em três partes:**
1. **Arquitetura do Sensor**: responsável por gerar os dados do sensor.
    * API-REST básica em Python que gerará os dados dos sensores. Baseados nos casos de exemplo.
2. **Arquitetura do IoT-Agent Suite** (IDAS) do FIWARE.
    * Responsável por centralizar os dados dos sensores e enviá-los para o Broker.
3. **Arquitetura do Broker**: responsável por processar os dados.
    * Servidor Orion Context Broker que irá receber os dados dos sensores e processá-los.
4. **Arquitetura do Cliente**: responsável por consumir os dados.
    * Aplicação que irá consumir os dados do broker.


#### Instalações de dependências
```sh
    $ pip install orionclient, requests
```


#### Setup

###### [Documentação Usada](https://github.com/telefonicaid/fiware-orion/blob/master/docker/README.md)


