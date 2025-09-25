from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional

app = FastAPI()

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str  

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_users():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:

        users = [
            User(username="user1", password="pass1"),
            User(username="user2", password="pass2"),
        ]
        for user in users:
            
            statement = select(User).where(User.username == user.username)
            existing_user = session.exec(statement).first()
            if not existing_user:
                session.add(user)
        session.commit()

create_db_and_users()


class LoginData(SQLModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginData):
    with Session(engine) as session:
        statement = select(User).where(User.username == data.username)
        user = session.exec(statement).first()
        if not user or user.password != data.password:
            raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
        return {"message": f"Bienvenido {user.username}"}
