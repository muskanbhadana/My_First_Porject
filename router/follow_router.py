from fastapi import APIRouter
from controller.follow import follows,followerfind,followingfind,Unblock,Unfollowed,blockUser
from schemas.follow_schemas import Follow,BlockData

router=APIRouter()

@router.post("/follow")
def add_employee(data:Follow):
    return follows(data)

@router.post("/unfollow")
def unfollow_user(data: Follow):
    return  Unfollowed(data)

@router.get("/following/{user_id}")
def add_employee(user_id:int):
    return followerfind(user_id)

@router.get("/follower/{user_id}")
def followeremployee(user_id:int):
    return followingfind(user_id)


@router.post("/block")
def block_data(data:BlockData):
    return blockUser(data)


@router.post("/unblock")
def unfollowed(data:BlockData):
    return Unblock(data)



