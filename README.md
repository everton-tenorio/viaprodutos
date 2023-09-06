<img src="https://github.com/evertonbsi/django-enket/blob/main/polls/Screenshot%202022-08-22%20at%2007-09-28%20frontend.png?raw=true"/>

**viaprodutos** é um sistema web feito em Django Rest Framework e Vuejs, com objetivo de pesquisar e listar produtos de lojas do grupo viavarejo(Casas Bahia, Extra e Ponto Frio) através de uma API que mostra informações como: Preço do produto, Descontos, disponibilidade do produto, etc.

O sistema possui um frontend simples e intuitivo que permite realizar a busca através de um único campo de texto, sendo necessário selecionar qual a loja escolhida, quantos itens terá em resultados na página e o nome do produto. *Ambos os filtros são obrigatórios.**

## Executar o projeto com Docker
Para facilitar a execução foi utilizado docker-compose que faz o build das as imagens e já sobe os containers em estado de execução com todas as dependências instaladas. Em cada arquivo Dockerfile são utilizadas portas padrões.

No diretório principal do projeto viaprodutos/ localize o arquivo docker-compose.yml e execute o comando no terminal:

```bash
docker-compose up -d
```
Verifique o estado dos containers executados:

```bash
docker container ls
```

Acesse a aplicação localmente em "http://localhost:8080".

## Rotas
Feito isso, a API irá tratar de buscar esses produtos na base disponível na internet de produtos do grupo viavarejo através de uma única rota que facilita o acesso as lojas, sendo feito também uma verificação por produto para selecionar preços e avisos quando o mesmo está fora de estoque.

## Django Rest Framework
O presente projeto serviu também para estudo desta tecnologia que permite criar APIs Restful, sendo executado como plugin do django ao ser instalado/configurado em settings.py do projeto principal, foi utilizado os recursos iniciais como serializers que serve de atalho para captação das informações na API pública e APIView para criar a API recebendo os dados da requisição validando de acordo com as regras implementadas e por fim responder com o metódo *Response()*.

## Vue
O framework frontend é utilizado separado da API com intuito de fornecer uma melhor visualização dos dados via JSON, foi utilizado recursos como Axios para fazer a ligação com a API.

## Considerações
viaprodutos é um projeto realizado para um teste sob as condições:
 - Extrair dados utilizando livre abordagem
 - Exibir dados no frontend em tempo real no momento da soliticação do usuário
 - Não é necessário persistir dados no DB
 - Instruções de execução no README.md
 - Adicional se o projeto estiver com docker/docker-compose

Everton.




