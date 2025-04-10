from django.urls import path
from .views import villas_beachfront, villas_party_friendly, villas_pet_friendly, villas_with_entertainment, ListVillaView,villas_with_pool,CreatVillaView ,CreateListVillaView,UpdateVillaView,DeleteVillaView,RetriveUpdateDeleteVillaView


urlpatterns = [
    path("villabeachfront/", villas_beachfront),
    path("villaparty/", villas_party_friendly),
    path("villapet/", villas_pet_friendly),
    path("villa/", villas_with_entertainment),
    path("villapooli/", villas_with_pool),
    path('new-list', ListVillaView.as_view()),
    path('create' ,CreatVillaView.as_view() ),
    path('update/<int:pk>' ,UpdateVillaView.as_view()),
    path('delete/<int:pk>' , DeleteVillaView.as_view()),
    path('create-list' , CreateListVillaView.as_view()),
    path('retrive-update-delete',RetriveUpdateDeleteVillaView.as_view())
    
]
