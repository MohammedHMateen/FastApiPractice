
from fastapi import FastAPI, HTTPException
from fastapi.params import Query

from model.user import *

test_app = FastAPI()
list_db = [
    User(
        id=2,
        name="A",
        gender=Gender.male,
        latitude=56.83948393,
        longitude=56.83948393
    ),
    User(
        id=1,
        name="B",
        gender=Gender.female
    )
]


@test_app.get("/a")
def root():
    db: str = "Alhamdulillah :)"
    return db


# to run this app do >> uvicorn filename:appname --reload


@test_app.get("/api/users")
def get_users():
    return list_db


@test_app.get("/api/users/{id}")
def get_users_by_id(uid: int):
    for user in list_db:
        if user.id == uid:
            return user
    raise HTTPException(
        status_code=404,
        detail=f"Can't find any user with id: {uid}"
    )


# With query parameters /api/users?uid=1
# Query Params with extra informations
# q2: bool = Query(True, description = "Query with extra bool info")
# q1: int = Query(..., ge=0),
@test_app.get("/api/users/")
def get_users_by_id_in_query(uid: int,
                             q1: int = Query(any, ge=0),
                             q2: bool = Query(True, description="Query with extra bool info")):
    listy = []
    for user in list_db:
        if user.id == uid:
            listy.append(user)
            listy.append(f"{q1}&&{q2}")
            return listy
    raise HTTPException(
        status_code=404,
        detail=f"Can't find any user with id: {uid}"
    )


@test_app.post("/api/users")
async def add_users(user: User) -> str:
    list_db.append(user)
    return "Added user with id:{}".format(user.id)


@test_app.delete("/api/users/{uid}")
async def del_users_by_id(uid: int) -> str:
    del_count = 0
    for user in list_db:
        if user.id == uid:
            del_count += 1
            list_db.remove(user)

    return f"Deleted {del_count} users with id: {uid}"
