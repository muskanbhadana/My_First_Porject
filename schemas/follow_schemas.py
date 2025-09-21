from pydantic import BaseModel

class Follow(BaseModel):
  followed_by:int
  followed_to:int
  

class BlockData(BaseModel):
    block_by: int
    block_to: int
    


