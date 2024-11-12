from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse 

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user

# /docs
# /redoc
