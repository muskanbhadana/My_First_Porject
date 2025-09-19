from pydantic import BaseModel
from typing import Optional,List

   
# post db----------------->

class UserPost(BaseModel):
    post_id:int
    user_id:int
    title:str
    content:str
    
# getall post------------------------->

class GetAll(BaseModel):
    post_id:Optional[List[UserPost]]=None
    
# postby id---------------------->
class Post_Get_By_User_Id(BaseModel):
    user_id:int
    message:str
    users:List[UserPost]=[]
# title------------------------>
class Post_get_by_Title(BaseModel):
       title:str
       posts:List[UserPost]=[]
       message:str
# count------------------->
class Post_count_By_User_Id(BaseModel):
    user_id: int
    message: str
    user: List[UserPost]   
    totalusers: int
