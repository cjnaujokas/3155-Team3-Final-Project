from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import complete_orders as model
from sqlalchemy.exc import SQLAlchemyError

# Complete Orders Controller
def create(db: Session, request):
    new_item = model.complete_orders(
        order_id=request.order_id
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

# Complete Orders Controller
def read_all(db: Session):
    try:
        result = db.query(model.complete_orders).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

# Complete Orders Controller
def read_one(db: Session, item_id):
    try:
        item = db.query(model.complete_orders).filter(model.complete_orders.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

# Complete Orders Controller
def update(db: Session, item_id, request):
    try:
        item = db.query(model.complete_orders).filter(model.complete_orders.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

# Complete Orders Controller
def delete(db: Session, item_id):
    try:
        item = db.query(model.complete_orders).filter(model.complete_orders.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
