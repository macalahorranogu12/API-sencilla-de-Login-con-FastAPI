El primer paso para el ejercicio es instalar api, el cual es una interfaz de programacion de aplicaciones, esto es para poder implementar un API REST a traver de FastAPI. 
Despues necesitamos hacer las siguientes importaciones para nuestro código: 
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
Ya que debemos hacer una base de datos "Quemada" desde el código. 
A continuacion vamos a proseguir con el la creacion de la base de datos creando una clase usando la importacion del sql
ademas de crear tambien la funcion que es la que va a agregar los usuarios y contraeeñas en la base de datos





# Ejemplos de ejecucion
Para el primer ejemplo. debemos ejecutar el siguiente comando  en la terminal : python -m uvicorn main:app --reload, lo cual nos dara el siguiente link: http://127.0.0.1:8000/docs
al abrirlo vamos a colocar el usuario y contraseña de ejemplo, el cual seria: user1, pass1. Y obtendremos como resultado lo siguiente: bienvenido user1, en caso de ser el user 2
nos daria: bienvenido user2.

Al poner un usuario o contaseña incorrecta, obtendremos un error como resultado, imprimiendo el mensaje: Usuario u contraseña incorrectos. 
