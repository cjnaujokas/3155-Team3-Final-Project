from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import complete_orders as controller
from ..schemas import complete_orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Complete Orders'],
    prefix="/complete_orders"
)


@router.post("/", response_model=schema.complete_ordersResource)
def create(request: schema.complete_ordersCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.complete_ordersResource])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.complete_ordersResource)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.complete_ordersResource)
def update(item_id: int, request: schema.complete_ordersUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
