# Banco de Dados

Para essa atividade vamos usar o PostgreSQL e o dbeaver

## O que é um Banco de Dados?

Um banco de dados é um sistema de armazenamento de dados eletrônico. Um sistema de gerenciamento de banco de dados (SGBD) é um software que permite aos usuários definir, criar, manter e controlar o acesso aos bancos de dados.

A vantagem de trabalhar com um banco de dados é que ele permite que você armazene dados em tabelas e, em seguida, recupere esses dados com consultas. Isso torna mais fácil para você organizar seus dados e torná-los mais acessíveis. Além de fornecer compressão de dados, um banco de dados também oferece segurança, backup e recuperação de dados.

## O que é um SGBD?

Um sistema de gerenciamento de banco de dados (SGBD) é um software que permite aos usuários definir, criar, manter e controlar o acesso aos bancos de dados. O PostgreSQL é um exemplo de um SGBD.

## O que é o PostgreSQL?

PostgreSQL é um sistema gerenciador de banco de dados objeto relacional (SGBD), desenvolvido como projeto de código aberto. Hoje é considerado um dos melhores SGBD de código aberto e é utilizado em diversos projetos ao redor do mundo.

## Para termos o PostgreSQL vamos usar o Docker

Quais são as formas de rodar PostgreSQL usando Docker?

### 1) Usando a imagem oficial do PostgreSQL

1. **Pull da Imagem do PostgreSQL**: Se você ainda não tem a imagem do PostgreSQL, pode obtê-la usando o comando `docker pull`:
    
    ```bash
    docker pull postgres
    ```
    
2. **Executando o Contêiner PostgreSQL**: Para iniciar um contêiner com PostgreSQL, use o comando `docker run`. Você pode especificar a senha do superusuário, o nome do banco de dados e o nome de usuário como variáveis de ambiente:
    
    ```bash
    docker run --name meu_postgres -e POSTGRES_PASSWORD=minha_senha -e POSTGRES_USER=meu_usuario -e POSTGRES_DB=meu_banco -p 5432:5432 -v meu_volume_postgres:/var/lib/postgresql/data -d postgres
    ```
    
    Substitua `minha_senha`, `meu_usuario` e `meu_banco` `meu_volume_postgres` pelos valores desejados.
    
    * `--name meu_postgres`: Define o nome do contêiner como `meu_postgres`.
    * `-e POSTGRES_PASSWORD=minha_senha`: Define a senha do superusuário para `minha_senha`.
    * `-e POSTGRES_USER=meu_usuario`: Cria um usuário com o nome `meu_usuario`.
    * `-e POSTGRES_DB=meu_banco`: Cria um banco de dados com o nome `meu_banco`.
    * * `-v meu_volume_postgres:/var/lib/postgresql/data`: Monta um volume chamado `meu_volume_postgres` na pasta `/var/lib/postgresql/data` dentro do contêiner. Se o volume `meu_volume_postgres` não existir, ele será criado automaticamente pelo Docker.
    * `-p 5432:5432`: Mapeia a porta 5432 do contêiner para a porta 5432 na máquina host.
    * `-d`: Executa o contêiner em background.
  

   * **Persistência de Dados**: Armazena os dados do banco de dados no volume `meu_volume_postgres`. Mesmo se o contêiner for removido, os dados permanecerão no volume e estarão disponíveis quando você criar um novo contêiner com o mesmo volume.
   * **Gerenciamento de Volume**: O Docker gerencia este volume, e você pode encontrar os dados armazenados no local de armazenamento de volumes do Docker no seu sistema host.

### 2) Criando um arquivo Dockerfile

O Dockerfile é um arquivo de texto que contém todas as instruções necessárias para criar uma imagem Docker. Você pode criar uma imagem Docker do PostgreSQL usando um Dockerfile. Aqui, vou mostrar como criar uma imagem Docker do PostgreSQL usando um Dockerfile.

1. **Criando um Dockerfile**: Crie um arquivo chamado `Dockerfile` e adicione o seguinte conteúdo:
    
    ```Dockerfile
    # Use the official PostgreSQL image as a base
    FROM postgres:latest
    
    # Set environment variables
    ENV POSTGRES_PASSWORD=minha_senha
    ENV POSTGRES_USER=meu_usuario
    ENV POSTGRES_DB=meu_banco
    
    # Expose the default PostgreSQL port
    EXPOSE 5432
    
    # Set the default command to run when starting the container
    CMD ["postgres"]
    
    ```

Após o Dockerfile estar pronto, você pode criar uma imagem Docker usando o comando `docker build`:

```bash
docker build -t minha_imagem_postgres .
```

* `-t meu_postgres`: Define o nome da imagem como `meu_postgres`.

Após a criação da imagem, você pode executar um contêiner com o comando `docker run`:

```bash
docker run --name meu_container_postgres -p 5432:5432 -v meu_volume_postgres:/var/lib/postgresql/data -d minha_imagem_postgres
```

* `--name meu_postgres`: Define o nome do contêiner como `meu_postgres`.
* `-p 5432:5432`: Mapeia a porta 5432 do contêiner para a porta 5432 na máquina host.
* `-v meu_volume_postgres:/var/lib/postgresql/data`: Monta um volume chamado `meu_volume_postgres` na pasta `/var/lib/postgresql/data` dentro do contêiner. Se o volume `meu_volume_postgres` não existir, ele será criado automaticamente pelo Docker.
* `-d`: Executa o contêiner em background.

## Segurança

Não podemos salvar as senhas no Dockerfile, pois ele é um arquivo de texto e qualquer um pode ver. Para isso vamos usar as variáveis de ambiente.

O ideal é que você crie um arquivo .env e coloque suas variáveis lá.

```bash
touch .env
```

Nesse arquivo vamos ter o código

```bash
POSTGRES_PASSWORD=minha_senha
POSTGRES_USER=meu_usuario
POSTGRES_DB=meu_banco
```

Agora vamos usar essas variáveis no nosso Dockerfile

```Dockerfile
# Use the official PostgreSQL image as a base
FROM postgres:latest

# Define arguments and then convert them to environment variables
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_DB

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}

# Expose the default PostgreSQL port
EXPOSE 5432

# Set the default command to run when starting the container
CMD ["postgres"]
```

Agora vamos criar nossa imagem

```bash
docker build -t minha_imagem_postgres --build-arg POSTGRES_PASSWORD=minha_senha --build-arg POSTGRES_USER=meu_usuario --build-arg POSTGRES_DB=meu_banco .
```

Agora vamos criar nosso contêiner

```bash
docker run --name meu_container_postgres -p 5432:5432 -v meu_volume_postgres:/var/lib/postgresql/data -d minha_imagem_postgres
```

## Acessando o Banco de Dados

Vamos usar o pgAdmin para acessar nosso banco de dados

O pgAdmin é um software de código aberto para gerenciamento de banco de dados PostgreSQL. Ele fornece uma interface gráfica para gerenciar e administrar bancos de dados PostgreSQL.

Para instalar o pgAdmin, vamos acessar o Docker Hub e buscar a imagem oficial e seguir os passos

[Docker Hub](https://hub.docker.com/)

### Conectar ao Banco de Dados

* Para se conectar a este banco de dados PostgreSQL, você deve usar obter o endereço IP do container docker
    
    ```bash
    docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nome_do_container_postgres
    ```
    
Após isso você pode acessar o pgAdmin no seu navegador e criar uma conexão com o banco de dados.

#### Vamos criar nossa tabela

```sql

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco NUMERIC(10,2)
);

```

#### Podemos inserir valores

```sql

INSERT INTO produtos (titulo, descricao, preco) VALUES 
('Cadeira Gamer', 'Cadeira confortável para fazer live', 1200.00),
('Workshop', 'Workshop de deploy', 100.00),
('Iphone', 'Iphone 14', 2000.00);

```

#### Podemos fazer uma consulta

```sql

SELECT * FROM produtos;

```

#### Podemos fazer um update

```sql

UPDATE produtos SET preco = 5000 WHERE id = 1;

```

#### Podemos fazer um delete

```sql

DELETE FROM produtos WHERE id = 1;

```

#### Podemos deletar n ossa tabela

```sql

DROP TABLE produtos;

```

## Acessando nosso Banco de Dados com Python

### Vamos usar para isso o SQLAlchemy

O SQLAlchemy é um ORM (Object Relational Mapper) para Python que facilita a criação de aplicações que utilizam bancos de dados relacionais. Ele fornece uma abstração de alto nível para a criação e manipulação de tabelas sem a necessidade de escrever SQL.

A vantagem de usar um ORM é que você pode escrever código Python para manipular o banco de dados, em vez de escrever SQL. Isso torna o código mais legível e mais fácil de manter.

Precisamos instalar as bibliotecas

```bash
pip install sqlalchemy psycopg2-binary
```

Vamos agora criar um arquivo chamado database.py

```bash
touch database.py
```

Nesse arquivo vamos ter o código

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criando a engine de conexão

engine = create_engine(DATABASE_URL)

# Criando a sessão

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
```

Todos os comandos SQL que você executou anteriormente podem ser executados usando o SQLAlchemy.

Para verificar como foi feita toda a operação de CRUD no SQLAlchemy, olhar a pasta SRC.

Porém, vamos realizar as operações de CRUD usando o FastAPI.

