import shutil
from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from schemas import UploadVideo, GetVideo, Message
from models import Video, User

video_router = APIRouter()


@video_router.post('/')
async def create_video(
    title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)
):
    info = UploadVideo(title=title, description=description)
    with open(f"{file.filename}", 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()
    return await Video.objects.create(file=file.filename, user=user, **info.dict())



@video_router.get('/video/{video_id}', response_model=GetVideo, responses={404: {'model': Message}})
async def get_one_video(video_id: int):
    video_db = await Video.objects.select_related('user').get(pk=video_id)
    return video_db
