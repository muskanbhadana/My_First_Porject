from pydantic import BaseModel
from typing import Optional,List

class Follow(BaseModel):
  follow_id:int
  follower_id:int
  following_id:int
  
  
# class User(BaseModel):
#   user_id:int
#   email:str
#   password:str
#   user_name:str
  
# class Follower(BaseModel):
#     following_id: int   
#     follower: List[User]  
#     message: str

# class FollowerResponse(BaseModel):
#     follower_id: int   
#     followering: List[User]   
#     message: str
















# class Follow (BaseModel):
#   follow_to :str
#   follow_by:str
  
# class Follow_id(BaseModel):
#     data:Optional[List[Follow]]=None
#     message:str

