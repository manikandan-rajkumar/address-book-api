from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.address import Address
from app.schemas.address import AddressCreate, AddressResponse, AddressUpdate
from app.services import address_service

router = APIRouter(prefix="/addresses", tags=["Addresses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    return address_service.create_address(db, address)


@router.put("/{address_id}", response_model=AddressResponse)
def update_address(
    address_id: int,
    data: AddressUpdate,
    db: Session = Depends(get_db),
):
    address = address_service.update_address(db, address_id, data)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    success = address_service.delete_address(db, address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}


@router.get("/nearby", response_model=List[AddressResponse])
def nearby_addresses(
    lat: float,
    lon: float,
    distance_km: float,
    db: Session = Depends(get_db),
):
    return address_service.get_nearby_addresses(db, lat, lon, distance_km)


@router.get("/", response_model=list[AddressResponse])
def get_all_addresses(db: Session = Depends(get_db)):
    return db.query(Address).all()


@router.get("/{address_id}", response_model=AddressResponse)
def get_address(address_id: int, db: Session = Depends(get_db)):
    address = db.get(Address, address_id)

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    return address
