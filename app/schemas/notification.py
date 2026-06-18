from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class ChannelEnum(str, Enum):
    SMS = "SMS"
    Email = "Email"
    Push = "Push"


class StatusEnum(str, Enum):
    Pending = "Pending"
    Sent = "Sent"
    Failed = "Failed"


class NotificationCreate(BaseModel):
    title: str
    message: str
    channel: ChannelEnum


class NotificationUpdate(BaseModel):
    status: StatusEnum


class NotificationOut(BaseModel):
    id: int
    title: str
    message: str
    channel: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True