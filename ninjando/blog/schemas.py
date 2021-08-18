from typing import List
from datetime import datetime
from ninja import Schema

class Category(Schema):
    id: int
    name: str




class CategoryParent(Category):
    parent: Category = None


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
    tag: List[Tag] = None
    category: Category
    published: bool
    viewed: int

class CreateComment(Schema):
    post_id: int = None
    text: str
    parent_id: int = None
    user_id: int = None

class Comment(CreateComment):
    id: int
    
    