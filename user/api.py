from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from . import schemas, services
from config import GOOGLE_CLIENT_ID

templates = Jinja2Templates(directory='templates')

user_router = APIRouter(tags=['auth'])


@user_router.get('/', response_class=HTMLResponse)
async def google_auth_button(request: Request):
    return templates.TemplateResponse(
        'auth.html', {'request': request, 'google_client_id': GOOGLE_CLIENT_ID})


@user_router.post('/google/auth', response_model=schemas.Token)
async def google_auth(jwtoken: schemas.UserCreate):
    user_id, token = await services.google_auth(jwtoken)
    return schemas.Token(id=user_id, token=token)
