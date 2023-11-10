from models.produto import Produto
from database.session import Session


def atualizar_produto(id, titulo=None, descricao=None, preco=None):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == id).first()
    if produto:
        if titulo:
            produto.titulo = titulo
        if descricao:
            produto.descricao = descricao
        if preco:
            produto.preco = preco
        session.commit()
    else:
        print(f"Produto com ID {id} não encontrado.")
    session.close()
