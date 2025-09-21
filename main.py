from fastapi import FastAPI

from  router.user_router import router 
from router.follow_router import routers
from router.post_router import router as post_router
app=FastAPI()
app.include_router (post_router)
app.include_router(router) 
app.include_router(routers) 
