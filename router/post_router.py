from fastapi import APIRouter

# Import your controller
from controller.user import user
from controller.post import user_post,getall,get_by_id,get_by_user_id,getbytitle,countpost
# Import your schemas
from schemas.post_schemas import UserPost,Post_count_By_User_Id,Post_Get_By_User_Id,Post_get_by_Title,GetAll
# -------------------------
router=APIRouter()
# -------------------------
# Post Endpoints
# -------------------------
@router.post("/post/{user_id}")
def user_create_post(user_id: int, data: UserPost):
    return user.post(user_id, data)


@router.get("/getallpost", response_model=GetAll)
def all_posts():
    return user.getall()


@router.get("/getbyid/{post_id}", response_model=Post_count_By_User_Id)
def get_post_by_id(post_id: int):
    return user.get_post_by_id(post_id)


@router.get("/getpostbyuser_id/{user_id}", response_model=Post_Get_By_User_Id)
def get_posts_by_user(user_id: int):
    return user.get_post_by_user_id(user_id)


@router.get("/posttitle/{title}", response_model=Post_get_by_Title)
def get_post_by_title(title: str):
    return user.get_by_title(title)


@router.get("/post/{user_id}", response_model=Post_count_By_User_Id)
def count_posts(user_id: int):
    return user.countpost(user_id)

