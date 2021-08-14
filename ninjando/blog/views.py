from ninja import NinjaAPI
from django.shortcuts import get_list_or_404
from . import models, schemas
from typing import List


api = NinjaAPI()

@api.get("/category", response=List[schemas.Category])
def gat_categoty(request):
    return models.Category.objects.filter(published=True)

@api.get("/post", response=List[schemas.Post])
def gat_list_post(request):
    return models.Post.objects.filter(published=True)    

@api.get("/post/{post_pk}", response=List[schemas.Post])
def gat_list_post(request, post_pk: int):
    return get_object_or_404(models.Post, published=True)