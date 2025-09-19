from fastapi import APIRouter

from controller.follow import follows
from schemas.follow_schemas import Follow

routers=APIRouter()

from controller.follow import follows
# followerfind,followingfind
from schemas.follow_schemas import Follow
# Follower,FollowerResponse

router=APIRouter()

@router.post("/follow")
def add_employee(data:Follow):
    return follows(data)

# @router.get("/following/{user_id}",response_model=Follower)
# def add_employee(user_id:int):
#     return followerfind(user_id)

# @router.get("/follower/{user_id}",response_model=FollowerResponse)
# def followeremployee(user_id:int):
#     return followingfind(user_id)



# @routers.post("/follow")
# def add_employee(data:Follow):
#     return follows(data)

# @routers.get("/get",response_model=Follow_id)
# def follow_get():
#     return get_all_follow()