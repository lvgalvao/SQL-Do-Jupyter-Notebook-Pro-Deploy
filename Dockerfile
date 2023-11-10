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
