# Ejemplos de ejecucion
Para el primer ejemplo. debemos ejecutar el siguiente comando  en la terminal : python -m uvicorn main:app --reload, lo cual nos dara el siguiente link: http://127.0.0.1:8000/docs
al abrirlo vamos a colocar el usuario y contraseña de ejemplo, el cual seria: user1, pass1. Y obtendremos como resultado lo siguiente: bienvenido user1, en caso de ser el user 2
nos daria: bienvenido user2.

Al poner un usuario o contaseña incorrecta, obtendremos un error como resultado, imprimiendo el mensaje: Usuario u contraseña incorrectos. 
