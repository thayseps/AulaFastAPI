from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Caitlyn', email='cupcake@gmail.com', password='kiramann'
    )

    session.add(user)
    session.commit()
    # session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'cupcake@gmail.com')
    )

    assert result.username == 'Caitlyn'
