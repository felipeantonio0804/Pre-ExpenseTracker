# Pre - Expense Tracker.
Proyecto creado con el framework django de python. 
Forma inicial donde se tiene unicamente la seccion de categorias y transaccione, administradas por el modulo admin de django.
Se crearon pantallas de funcionalidad principal:

/transactions/
/transactions/5
/transactions/details_category/5
/transactions/details_consult_transaction/5
/transactions/details_results_category/5

Ademas se hace el uso de la aplicacion de auth. Para temas de autentificacion y autorizacion.

## Cómo instalar el proyecto.
1. Lo primero que debes hacer es clonar éste repositorio y navegar a la carpeta contenedora del archivo 'manage.py'.

2. Una vez tengas clonada la carpeta de la aplicación asegurate de tener instalados los requerimientos de las librerias de python, con el comando `pip install requirements.txt`

3. Tambien es posible correr el programa dentro de un contenedor de docker, donde se deben de correr los comandos siguientes, Esto es como un extra, pero corriendolo local a la maquina tambien funciona.
```bash
docker build -t docker-django .
docker run -p 8000:8000 docker-django
docker run -d -p 8000:8000 -v [pathFolderContainerOfFile_manage.py]:/code docker-django
docker logs --follow [idContainer]
docker exec -it [idContainer] /bin/sh   
Dentro de la consola del contenedor =>  python manage.py migrate
Dentro de la consola del contenedor =>  python manage.py test
```

## Cómo ver la aplicación.
1. Para ver la aplicación debes correr el comando `python manage.py runserver` en tu terminal.

2. Una vez el comando haya ejecutado ve a la url `http://127.0.0.1:8000/` para ver el home de la aplicación, en donde se tendra que crear usuario o por lo menos un superusuario para poder entrar a explorar las pantallas mediante el comando `python manage.py createsuperuser`

