from models.produto import Produto
from database.session import Session


def consultar_produtos():
    session = Session()
    produtos = session.query(Produto).all()
    session.close()
    return produtos
