FROM mcr.microsoft.com/mssql/server


# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app


# Switch back to mssql user and run the entrypoint script
USER mssql
ENTRYPOINT /bin/bash ./entrypoint.sh
