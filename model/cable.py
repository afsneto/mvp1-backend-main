from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Cable(Base):
    __tablename__ = 'cabo'

    id = Column("pk_cable", Integer, primary_key=True)
    nome = Column(String(60), unique=True)
    tipo = Column(String(60))
    diametro = Column(Float)
    quantidade = Column(Integer)
    peso = Column(Float)
    capacidade = Column(Integer)
    observacao = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str, tipo: str, diametro: float, quantidade: int, peso: float, capacidade: str,
                 observacao: str, data_insercao: Union[DateTime, None] = None):
        """
        Cria uma instância do cabo

        Arguments:
            nome: nome do cabo
            tipo: tipo da liga
            diametro: diametro cabo [mm]
            quantidade: quantidade [km]
            peso: peso [kg/km]
            capacidade: corrente suportada [A]
            observacao: observações adicionais sobre a planta
            data_insercao: data de inserção da planta no banco de dados
        """
        self.nome = nome
        self.tipo = tipo
        self.diametro = diametro
        self.quantidade = quantidade
        self.peso = peso
        self.capacidade = capacidade
        self.observacao = observacao

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
