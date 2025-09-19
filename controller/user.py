from  fastapi import HTTPException
import random
user_db = [
    {"user_id": 1, "user_name": "muskan", "email": "alice.sharma@example.com", "password": "alice123"},
    {"user_id": 2, "user_name": "anmole", "email": "ravi.kumar@example.com", "password": "raviSecure!"},
    {"user_id": 3, "user_name": "pooja", "email": "meena.patel@example.com", "password": "meena@456"},
    {"user_id": 4, "user_name": "annu", "email": "john.doe@example.com", "password": "johnPassword"},
    {"user_id": 5, "user_name": "tanu", "email": "sara.ali@example.com", "password": "saraAli789"}
]

invalid_chars=["@","#","$","&","*","%"]

def singup(data):
    if not data.email or not data.user_name:
        raise HTTPException (status_code=400,detail="email and password is required")
    if not data.password:
        raise HTTPException(status_code=404,detail="password is required")
    for i in user_db:
            if i["email"]==data.email :
                 raise HTTPException(status_code=404,detail="email not valid")
            if i["user_name"]==data.user_name:
               raise HTTPException(status_code=404,detail="user_name not valid")
    for im in invalid_chars:
        if len(data.password)>=8:
            if im in data.password:
              new=data.dict()
              user_db.append(new)
              print("after user_db",user_db)
              return {"message":"user add","data":new}
    raise HTTPException(status_code=404,detail="password not valid")  
                
                
# login
def login(data):
    for i in user_db:
        if i["password"]!=data.password and  i["email"]!=data.email:
             raise HTTPException(status_code=404,detail=" password   and email not valid")
    return{"message":"login suc","user_data":user_db}

def otpget():
    otp=random.randint(1000,9999)
    return otp
otp=[]

# forget-------------------->
def user_forget(data):
    for  i in user_db:
        if i["password"]==data.password:
           otp=otpget()
           return {"message":"get otp","otp":otp}
    raise HTTPException(status_code=404,detail="old password  not match")


# update----------------------->
def user_update(update):
    for user in user_db:
        if user["password"] == update.old_password:
            if len(update.new_password) >= 8:
                for n in invalid_chars:
                    if n  in update.new_password:
                     user_data=n
                     user_db.append(user_data)
            return {"message": "Password updated successfully"}
        raise HTTPException(status_code=400, detail="New password must be at least 8 characters")
    raise HTTPException(status_code=404, detail="Old password not matched")


# delete/-------------->
def user_delete(data):
    for i in user_db:
        if i["user_id"]==data.user_id:
            user_db.remove(i)
            return {"message": "Password deleter successfully"}
    
    raise HTTPException(status_code=404,detail="user_id  not match")
