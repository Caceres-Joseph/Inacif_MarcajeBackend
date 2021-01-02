

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
```
Create Super User
```
Username: root
Email: jospehccaceres@gmail.com
Password: 123



docker-compose run web 


coverage run manage.py test apiM02_users -v 2



## Test

Para ejecutar los test
```
python manage.py test

coverage run manage.py test whatever -v 2
```

Run coverage:
```
$ coverage run manage.py test whatever -v 2
```
Use verbosity level 2, -v 2, for more detail. You can also test your entire Django Project at once with this command: coverage run manage.py test -v 2.

Build your report to see where testing should begin:
```
$ coverage html
```