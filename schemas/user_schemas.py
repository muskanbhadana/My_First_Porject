from pydantic import BaseModel
from typing import Optional,List
# user------------>
class User(BaseModel):
    user_id:int
    user_name:str
    email:str
    password:str
# getall------------->
class UserResponse(BaseModel):
    data:Optional[User]=None
    
# login------------------>
class Login(BaseModel):
    password:str
    email:str
    
# otp------------------>
    
class OtpGet(BaseModel):
    otp:int
    message:str
    
# updatepassword---------------->
class Password(BaseModel):
    password:str
  
class Update_Password(BaseModel):
    new_password:str
    old_password:str
# delete--------------------->
class OutData(BaseModel):
    user_id:int
 