from fastapi import HTTPException

post_db=[{"post_id":104,"user_id":11,"title":"hii","content":"Rainy Day"},
  {"post_id":101, "user_id":11, "title":"hii", "content":"Rainy Day"},
  {"post_id":102, "user_id":13, "title":"my cat", "content":"She climbed the fridge today!"},
  {"post_id":103, "user_id":14, "title":"school fun", "content":"We had a paper plane contest!"}
]

# post data------------->
# post data------------->
def user_post(data):
    for i  in post_db:
        if i["user_id"]!=data.user_id:
            raise HTTPException(status_code=404,detail="user_id  not match")
    post_db.append(data)
    return {"message":"post successfully","posted data":data}
            
        
#    getallpost     
def getall():
    if post_db:
          return{"message":"get all post ","post_id":post_db}
    raise HTTPException(status_code=400,detail="postid not match")
            
# postbyid--------------->
def get_by_id(post_id):
    for i in post_db:
        if i["post_id"]==post_id:
             return{"message":"get all post ","post_id":i}
    
    raise HTTPException(status_code=404,detail="post_id not match")


def get_by_user_id(user_id):
    user=[]
    for i in post_db:
        if i["user_id"]==user_id:
            user.append(i)
    if not user:
        raise HTTPException (status_code=404,detail="user_id not match ")
    return {
        "message":"get all post by user",
            "user_id":user_id,
            "users":user}
            

# post get by title---------------->

def getbytitle(title):
    ti = []
    for i in post_db:
        if i["title"] == title:
            ti.append(i)

    if not ti:
        raise HTTPException(status_code=404, detail="title not found")

    return {
        "message": "get by title",
        "title": title,
        "posts":ti
    }

# countpost--------------------> 
def countpost(user_id: int):
    user_posts = []
    for i in post_db:
        if i["user_id"] == user_id:
            user_posts.append(i)

    if not user_posts:
        raise HTTPException(status_code=404, detail="user_id not match")

    return {
        "message": "get all post by user",
        "user_id": user_id,
        "user": user_posts,             
        "totalusers": len(user_posts)   
    }

    
    
    