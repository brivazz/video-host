from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    # video: UploadVideo
    title: str
    description: str


class Message(BaseModel):
    message: str
