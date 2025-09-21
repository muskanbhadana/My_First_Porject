
    
from fastapi import HTTPException
follow_db=[ 
    {"followed_by": 2, "followed_to": 1} ]

user_db = [{"user_id": 1, "user_name": "muskan", "email": "muskan@example.com", "password": "alice123"},
    {"user_id": 2, "user_name": "anmole", "email": "anmole@example.com", "password": "raviSecure!"},]

def follows(data):
    for i in follow_db:
        if  i["followed_by" ]==data.followed_by and  i["followed_to"]==data.followed_to:
             return {"message":"your data  already added successfully"}
    for  u in user_db:
        if u["user_id"]==data.followed_by:
            for i in user_db:
                if i["user_id"]==data.followed_to:
                   follow_db.append(data.dict())
                   
                   return {" following_by ": data.followed_by,    "message": "your data added successfully"}
            raise HTTPException(status_code=400,detail= " followed_to not match")
    raise HTTPException(status_code=400,detail= "followed_by not match")
 
def Unfollowed(data):
    for i in follow_db:
       if i["followed_by"] == data.followed_by and i["followed_to"] == data.followed_to:  
            follow_db.remove(i)
            return { "message": "your data unfollowed successfully"}
    raise HTTPException(status_code=400,detail= "followed_by ad follow_to not match")
 

def  followerfind(user_id):
    follower=[]
    for i in follow_db:
        if i ["followed_to"] ==user_id:
           follower.append(i)
    if  follower:
        for b in block_db:
            if b["block_to"] in follower:
                follower.remove(b["block_to"])
    if not follower:
        raise HTTPException (status_code=400,detail="Your  user_id not found")
    return {
        "followed_bu": user_id,    
        "follower": follower,  
        "message": "data found successfully"
    }

def  followingfind(user_id):
    following=[]
    for i in follow_db:
        if i ["followed_by"] == user_id:
            following.append(i)
    if following:
        for b in block_db:
            if b["block_by"] in following:
                following.remove(b["block_by"])
    if not following:
        raise HTTPException (status_code=400,detail="not found")
    return {"followed_to": user_id,"followed": following, "message": "Your followed successfully" }      

block_db=[]
def blockUser(data):
    for i in block_db:
        if i["block_by"]==data.block_by and i["block_to"]==data.block_to:
             raise HTTPException(status_code=400, detail="Already blocked this user")
    
    block_db.append(data.dict())
    return {"block_by": data.block_by, "block_to": data.block_to, "message": "User block successfully"}
           
  

def Unblock (data):
    for i in block_db:
        if i["block_by"]==data.block_by and i["block_to"]==data.block_to:
            block_db.remove(i)
            return {"message": "User unblock  successfully"}
    raise HTTPException (status_code=400,detail=" block data not match")
            
   


