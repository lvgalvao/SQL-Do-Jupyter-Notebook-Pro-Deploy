from database.init_db import init_db
from crud.create import adicionar_produto
from crud.read import consultar_produtos
from crud.update import atualizar_produto
from crud.delete import deletar_produto

# Inicializar banco de dados e criar tabelas
init_db()

# Adicionar produtos
adicionar_produto("Cadeira Gamer", "Cadeira confortável para jogos", 1200.00)
adicionar_produto("Workshop Python", "Workshop sobre Python", 300.00)

# Consultar produtos
produtos = consultar_produtos()
for produto in produtos:
    print(produto.titulo, produto.preco)

# Atualizar produto
atualizar_produto(1, preco=1500.00)

# Deletar produto
deletar_produto(2)

# Consultar produtos após atualizações
produtos = consultar_produtos()
for produto in produtos:
    print(produto.titulo, produto.preco)
