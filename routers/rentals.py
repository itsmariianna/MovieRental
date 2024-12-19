from fastapi import APIRouter, Depends
from models.schemas import Rental
from utils.auth_utils import get_current_user
from routers.helper import read_json, write_json

router = APIRouter()

RENTALS_FILE = "json_files/rentals.json"


# Rent a movie 
@router.post("/rentals")
def rent_movie(rental: Rental, current_user: dict = Depends(get_current_user)):
    all_rentals = read_json(RENTALS_FILE)
    user_name = current_user["username"]
    rental_data = rental.dict()
    rental_record = {"user": user_name, **rental_data}
    all_rentals.append(rental_record)
    write_json(RENTALS_FILE, all_rentals)
    return rental


# Retrieve the rental history for the authenticated user
@router.get("/rentals")
def get_rentals(current_user: dict = Depends(get_current_user)):
    all_rentals = read_json(RENTALS_FILE)
    user_rentals = []
    current_username = current_user["username"]
    for rental in all_rentals:
        if rental["user"] == current_username:
            user_rentals.append(rental)
    return user_rentals