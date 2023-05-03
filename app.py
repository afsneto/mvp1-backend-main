from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Cable
from schemas import *


info = Info(title="API para gerenciamento de cabos armazenados",
            version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# Definindo tags
home_tag = Tag(name="Documentação", description="Documentação da API.")
cable_tag = Tag(
    name="API", description="Adição, visualização e remoção de cabos.")

# Implementando as rotas

# Rota para documentação swagger


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger - abre a documentação swagger da API proposta.
    """
    return redirect('/openapi/swagger')

# Rota para adicionar um cabo (POST)


@app.post('/cable', tags=[cable_tag],
          responses={"200": CableViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cable(form: CableSchema):
    """Adiciona um novo cabo e retorna uma representação do cabo.
    """
    cable = Cable(
        nome=form.nome,
        tipo=form.tipo,
        diametro=form.diametro,
        quantidade=form.quantidade,
        peso=form.peso,
        capacidade=form.capacidade,
        observacao=form.observacao
    )

    try:
        # criando conexão com a base de dados
        session = Session()
        # adicionando o cabo
        session.add(cable)
        # efetivando o comando de inclusão de novo cabo na tabela
        session.commit()
        return apresenta_cable(cable), 200

    except IntegrityError:
        # retorna erro caso já haja um cabo com o mesmo nome cadastrado na tabela
        # ou outro erro de integridade
        error_msg = "Cabo de mesmo nome já existente na base."
        return {"message": error_msg}, 409

    except Exception:
        # caso ocorra um erro diferente dos anteriores
        error_msg = "Não foi possível salvar novo item."
        return {"message": error_msg}, 400


# Rota para buscar todas as plantas cadastradas (GET)
@app.get('/cables', tags=[cable_tag],
         responses={"200": ListagemCablesSchema, "404": ErrorSchema})
def get_plantas():
    """Faz a busca por todos os cabos cadastrados e retorna uma representação da listagem dos cabos.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cables = session.query(Cable).all()

    if not cables:
        # se não há cabos cadastrados
        return {"cabos": []}, 200
    else:
        # retorna a representação de cabos
        print(cables)
        return apresenta_cables(cables), 200


# Rota para apagar um cabo pelo id (DELETE).
@app.delete('/cable', tags=[cable_tag],
            responses={"200": CableDelSchema, "404": ErrorSchema})
def del_planta(query: CableBuscaSchema):
    """Deleta um cabo a partir do id informado e retorna uma mensagem de confirmação da remoção.
    """
    cable_id = query.cable_id

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cable).filter(Cable.id == cable_id).delete()
    session.commit()

    if count:
        # retorna a mensagem de confirmação e o id da planta removida
        return {"message": "Cabo removido.", "id": cable_id}
    else:
        # se o cabo não foi encontrado, retorna mensagem de erro
        error_msg = "Cabo não encontrado na base de dados."
        return {"message": error_msg}, 404
