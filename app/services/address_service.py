from sqlalchemy.orm import Session
from geopy.distance import geodesic
from typing import List
import logging

from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate

logger = logging.getLogger(__name__)


def create_address(db: Session, address: AddressCreate) -> Address:
    db_address = Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    logger.info(f"Address created with id={db_address.id}")
    return db_address


def update_address(db: Session, address_id: int, data: AddressUpdate) -> Address:
    address = db.get(Address, address_id)
    if not address:
        logger.warning(f"Address id={address_id} not found for update")
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(address, key, value)

    db.commit()
    db.refresh(address)
    logger.info(f"Address updated id={address_id}")
    return address

def delete_address(db: Session, address_id: int) -> bool:
    address = db.get(Address, address_id)
    if not address:
        logger.warning(f"Address id={address_id} not found for delete")
        return False

    db.delete(address)
    db.commit()
    logger.info(f"Address deleted id={address_id}")
    return True


def get_nearby_addresses(
    db: Session,
    latitude: float,
    longitude: float,
    distance_km: float,
) -> List[Address]:

    addresses = db.query(Address).all()
    nearby = []

    for addr in addresses:
        dist = geodesic(
            (latitude, longitude),
            (addr.latitude, addr.longitude),
        ).km

        if dist <= distance_km:
            nearby.append(addr)

    logger.info(
        f"Found {len(nearby)} addresses within {distance_km} km"
    )

    return nearby