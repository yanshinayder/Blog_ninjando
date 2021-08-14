from typing import List
from datetime import datetime
from ninja import Schema

class Category(Schema):
    id: int
    name: str
    parent_id: int = None


class Tag(Schema):
    id: int
    name: str


class Post(Schema):
    id: int 
    author_id: int
    title: str   
    mini_text: str
    text: str
    created_date: datetime  
    published_date: datetime  
    image: str
    # tag: List[int] = None
    category_id: int
    published: bool
    viewed: int
    

class Comment(Schema):
    id: int
    user_id: int = None
    post_id: int = None
    text: str
    parent_id: int = None