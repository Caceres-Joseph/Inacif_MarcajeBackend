

# Base de datos

# Primera vez se levantan los contenedores
Primero: Hay que crear una base de datos llamada DB_api
El scritp se encuentra en /db/setup.sql

El comando para cargar el script es:

```
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@55w0rd -d master -i /tmp/setup.sql
```

SELECT name FROM SYSOBJECTS WHERE xtype = 'U';
GO


# Django

## Migración
Primera migración
```
python manage.py migrate
```
Demás migraciones
```
python manage.py makemigrations
```

## Crear app
```
python manage.py startapp apiM01_login
python manage.py startapp apiM02_users
```

## Crear un super-usuario

Create Super User

```
$ python manage.py createsuperuser
```
Username: root
Email: jospehccaceres@gmail.com
Password: 123
