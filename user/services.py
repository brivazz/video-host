from fastapi import HTTPException

from . import tokenizator
from google.oauth2 import id_token
from google.auth.transport import requests

from . import schemas, models
from config import GOOGLE_CLIENT_ID


GOOGLE_CLIENT_ID = GOOGLE_CLIENT_ID


async def create_user(user: schemas.User) -> models.User:
    _user = await models.User.objects.get_or_create(**user)#.dict())
    return _user[0].id


async def google_auth(jwtoken: schemas.UserCreate) -> tuple:
    try:
        idinfo = id_token.verify_oauth2_token(jwtoken.token, requests.Request(), GOOGLE_CLIENT_ID)
    except ValueError:
        raise HTTPException(403, "Bad code")
    user_id = await create_user(
        {'username': idinfo['name'], 'email': idinfo['email'], 'avatar': idinfo['picture']})
    internal_token = tokenizator.create_token(user_id)
    return user_id, internal_token.get("access_token")
