from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurando a conexão com o banco de dados
DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

# Criando a engine de conexão
# Uma engine é um objeto que gerencia as conexões com o banco de dados e executa as instruções SQL
# Cada engine é específica para um banco de dados, então, se você quiser conectar-se a um banco de dados diferente,
# precisará criar uma nova engine.

engine = create_engine(DATABASE_URL)

# Criando a sessão
# Uma sessão é um objeto que representa uma conexão com o banco de dados.
# A sessão é usada para emitir comandos SQL e manipular os resultados obtidos.
# A sessão é criada a partir de uma engine.

Session = sessionmaker(bind=engine)

Base = declarative_base()


# Definindo o modelo de dados
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)


# Criando a tabela
Base.metadata.create_all(bind=engine)
