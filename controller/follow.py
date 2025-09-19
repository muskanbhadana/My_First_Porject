from fastapi import HTTPException
follow_db=[ 
    {"follower_id": 1, "following_id": 2,"follow_id":101},  
   {"follower_id": 2, "following_id": 1,"follow_id":102}  ]

user_db = [{"user_id": 1, "user_name": "muskan", "email": "muskan@example.com", "password": "alice123"},
           
    {"user_id": 2, "user_name": "anmole", "email": "anmole@example.com", "password": "raviSecure!"},
    {"user_id": 3, "user_name": "pooja", "email": "pooja@example.com", "password": "meena@456"},]

def follows(data):
    if data.follower_id==data.following_id:
         raise HTTPException(status_code=400,detail= "both equal")
    for  u in user_db:
        if u["user_id"]==data.follower_id:
            for i in user_db:
                if i["user_id"]==data.following_id:
                    follow_db.append(data.dict())
                    print (follow_db,"no")
                    return { "follow_to": data.follower_id," following_by ": data.following_id,   "message": "your data added successfully"}
            raise HTTPException(status_code=400,detail= "following_id not match ")
    raise HTTPException(status_code=400,detail= " follower_id not match ")

# def  followerfind(user_id):
#     follower=[]
#     for i in follow_db:
#         if i ["follower_id"] == user_id:
#             for u in user_db:
#                 if u["user_id"]==i["following_id"]:
#                     follower.append(u)
#     if not follower:
#         raise HTTPException (status_code=400,detail=" not found")
    
#     return { "following_id": user_id,"follower": follower, "message": "data found"}

# def  followingfind(user_id):
#     following=[]
#     for i in follow_db:
#         if i ["following_id"] == user_id:
#             for u in user_db:
#                 if u["user_id"]==i["follower_id"]:
#                     following.append(u)
#     if not following:
#         raise HTTPException (status_code=400,detail="not found")
#     return {
#         "following_id": user_id,    
#         "follower": following,  
#         "message": "data found"
#     }        
    
    



