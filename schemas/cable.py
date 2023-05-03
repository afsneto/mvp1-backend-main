from typing import Optional, List
from pydantic import BaseModel
from model.cable import Cable


class CableSchema(BaseModel):
    """ Define como um novo cabo inserido na base deve ser representado.
    """
    nome: str = "Rail"
    tipo: str = "ACSR"
    diametro: float = 29.6
    quantidade: Optional[int] = 12
    peso: float = 1600
    capacidade: int = 980
    observacao: str = "Cabo condutor com alma de aço"


class CableBuscaSchema(BaseModel):
    """ Define como será a estrutura que representa a busca de um cabo pelo seu id.
    """
    cable_id: int = 1


def apresenta_cables(cables: List[Cable]):
    """ Retorna uma representação de cabos seguindo o schema definido em cableViewSchema.
    """
    result = []
    for cable in cables:
        result.append({
            "id": cable.id,
            "nome": cable.nome,
            "tipo": cable.tipo,
            "diametro": cable.diametro,
            "quantidade": cable.quantidade,
            "peso": cable.peso,
            "capacidade": cable.capacidade,
            "observacao": cable.observacao
        })

    return {"cables": result}


class CableViewSchema(BaseModel):
    """ Define como uma cable será retornada.
    """
    id: int = 1
    nome: str = "Rail"
    tipo: str = "ACSR"
    diametro: float = 29.6
    quantidade: Optional[int] = 12
    peso: float = 1600
    capacidade: int = 980
    observacao: str = "Cabo condutor com alma de aço"


class CableDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção de uma cable.
    """
    message: str
    id: int


def apresenta_cable(cable: Cable):
    """ Retorna uma representação da cable seguindo o schema definido em CableViewSchema.
    """
    return {
        "id": cable.id,
        "nome": cable.nome,
        "tipo": cable.tipo,
        "diametro": cable.diametro,
        "quantidade": cable.quantidade,
        "peso": cable.peso,
        "capacidade": cable.capacidade,
        "observacao": cable.observacao
    }


class ListagemCablesSchema(BaseModel):
    """ Define como uma listagem de cables será retornada.
    """
    cables: List[CableViewSchema]
