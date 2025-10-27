from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    post_title: str
    post_url: str

class Posts(BaseModel):
    posts: List[Post]

class Detail(BaseModel):
    navbar_title: str
    navbar_title_url: str

class Details(BaseModel):
    titles: List[Detail]
