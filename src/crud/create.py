from models.produto import Produto
from database.session import Session


def adicionar_produto(titulo, descricao, preco):
    session = Session()
    novo_produto = Produto(titulo=titulo, descricao=descricao, preco=preco)
    session.add(novo_produto)
    session.commit()
    session.close()
