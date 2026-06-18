from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.models.notification import Notification
from app.models.user import User
from app.schemas.notification import NotificationCreate, NotificationUpdate, NotificationOut

router = APIRouter()


@router.post("/", response_model=NotificationOut)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_notification = Notification(
        title=notification.title,
        message=notification.message,
        channel=notification.channel.value,
        owner_id=current_user.id
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification


@router.get("/", response_model=List[NotificationOut])
def get_notifications(
    title: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Notification).filter(Notification.owner_id == current_user.id)

    if title:
        query = query.filter(Notification.title.contains(title))

    if status:
        query = query.filter(Notification.status == status)

    return query.all()


@router.get("/{notification_id}", response_model=NotificationOut)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.owner_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    return notification


@router.put("/{notification_id}", response_model=NotificationOut)
def update_notification_status(
    notification_id: int,
    update_data: NotificationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.owner_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    notification.status = update_data.status.value
    db.commit()
    db.refresh(notification)
    return notification


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.owner_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    db.delete(notification)
    db.commit()
    return {"message": "Notification deleted successfully"}