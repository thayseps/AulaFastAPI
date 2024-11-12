from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)   # arrange

    response = client.get('/')  # act

    assert response.status_code == HTTPStatus.OK   # assert
    assert response.json() == {'message': 'Olá mundo!'}

def test_read_root_deve_retornar_ok_e_ola_mundo_em_html():
    client = TestClient(app)   # arrange

    response = client.get('/home')  # act

    assert response.status_code == HTTPStatus.OK   # assert
    assert '<h1>Olá, mundo!</h1>' in response.text
