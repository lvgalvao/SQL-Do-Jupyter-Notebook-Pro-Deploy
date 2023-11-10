from models.produto import Produto
from database.session import Session


def deletar_produto(id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == id).first()
    if produto:
        session.delete(produto)
        session.commit()
    else:
        print(f"Produto com ID {id} não encontrado.")
    session.close()
