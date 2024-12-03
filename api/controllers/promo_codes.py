from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promo_codes as model
from sqlalchemy.exc import SQLAlchemyError

# Promo Codes Controller
def create(db: Session, request):
    new_item = model.Promo_Codes(
        code=request.code,
        expiration=request.expiration,
        description=request.description
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

# Read all promo codes
def read_all(db: Session):
    try:
        result = db.query(model.Promo_Codes).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

# Read one promo code
def read_one(db: Session, item_id):
    try:
        item = db.query(model.Promo_Codes).filter(model.Promo_Codes.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

# Update a promo code
def update(db: Session, item_id, request):
    try:
        item = db.query(model.Promo_Codes).filter(model.Promo_Codes.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

# Delete a promo code
def delete(db: Session, item_id):
    try:
        item = db.query(model.Promo_Codes).filter(model.Promo_Codes.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
