# Como executar a API

Clonar o repositório e acessar o diretório raiz (mvp1-backend) pelo terminal para executar os comandos abaixo.

Criar um ambiente virtual. No windows, usar:
```
$ py -m venv env
```
Ativar o ambiente virtual, executar o comando abaixo (para Windows):

```
$ .\env\Scripts\activate
```
Instalar as libs python listadas no `requirements.txt`.
```
(env)$ pip install -r requirements.txt
```

Para ativar a API, executar o comando abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
Abra [http://localhost:5000/][def] no navegador para verificar o status da API em execução. 

Deverá ser exibida a página inicial com a documentação em formato swagger da API com as rotas implementadas.

[def]: http://localhost:5000/
