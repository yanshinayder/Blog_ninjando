from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from . import models, schemas
from typing import List


api = NinjaAPI()

@api.get("/category", response=List[schemas.CategoryParent])
def get_categoty(request):
    return models.Category.objects.filter(published=True)

@api.get("/post", response=List[schemas.Post])
def get_list_post(request):
    return models.Post.objects.filter(published=True)    

@api.get("/post/{post_pk}", response=schemas.Post)
def get_single_post(request, post_pk: int):
    return get_object_or_404(models.Post, published=True)        


@api.post("/comment", response=schemas.Comment)    
def create_comment(request, comment: schemas.CreateComment):
    return models.Comment.objects.create(**comment.dict())


