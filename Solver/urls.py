from django.urls import path
from .views import *

urlpatterns = [
    path("",base,name="base"),

    # user
    path("User",get_all_carr,name="list_u"),
    path("detail_u/<int:pk>",get_by_id,name="detail_u"),
    path("update_u/<int:pk>",update,name="update_u"),
    path("create_u",add,name="create_u"),
    path("delete_u/<int:pk>",delete,name="delete_u"),
    
    # Category
    path("Category",get_all_carr1,name="list_c"),
    path("detail_c/<int:pk>",get_by_id1,name="detail_c"),
    path("update_c/<int:pk>",update1,name="update_c"),
    path("create_c",add1,name="create_c"),
    path("delete_c/<int:pk>",delete1,name="delete_c"),
    
    # Aplication
    path("Talant",get_all_carr11,name="list_m"),
    path("detail_m/<int:pk>",get_by_id11,name="detail_m"),
    path("update_m/<int:pk>",update11,name="update_m"),
    path("create_m",add11,name="create_m"),
    path("delete_m/<int:pk>",delete11,name="delete_m"),
    
    path("Aplication",get_all_carr111,name="list_o"),
    path("detail_o/<int:pk>",get_by_id111,name="detail_o"),
    path("update_o/<int:pk>",update111,name="update_o"),
    path("create_o",add111,name="create_o"),
    path("delete_o/<int:pk>",delete111,name="delete_o")
]