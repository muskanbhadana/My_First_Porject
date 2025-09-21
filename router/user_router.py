# -------------------------
from fastapi import APIRouter

# Import your controller
from controller  import user
# from controller.user import singup,login,otpget,user_forget,user_update,user_delete
# Import your schemas
from schemas.user_schemas import Password,Update_Password,User,Login,User,OutData,UserResponse,OtpGet
# -------------------------
router=APIRouter()
# -------------------------


# User / Auth Endpoints
# -------------------------

@router.post("/signup")
def user_add(data: User):
    return user.add(data)


@router.post("/login")
def login_user(login_data: Login):
    return user.login(login_data)


# @router.get("/otp", response_model=)
# def get_otp(otp: int):
#     return {"message": "get your otp", "otp": otp}


@router.patch("/forget")
def password_forget(forget: UserResponse):
    return user.forget(forget)


@router.patch("/update")
def user_password_update(update: Update_Password):
    return user.update(update)


@router.delete("/user")
def delete_user(out: OutData):
    return user.delete(out)

