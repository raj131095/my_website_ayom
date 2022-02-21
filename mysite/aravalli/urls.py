from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name="index"),
    path("home", views.home_page, name="home"),
    path("profile/login", views.login_view, name="login"),
    path("profile/logout", views.logout_view, name="logout"),
    path("profile/register", views.register, name="register"),
    path ("create", views.create, name="create_shop"),
    path("sucess",views.submit, name="submit"),
    path("file/", views.shopdata, name="shop"),
    path("file/1223<str:pk>223/23232/profile_page/7862/full_details/12902622",views.profilepage, name="profilepage"),
    path('file/2453<str:pk>2573/new2/45735/profile_page/3524/full_details/12903746', views.upload_image,name="uploadimage"),
    path('active', views.Active_list, name="activelist"),
    path('detail/6246<str:pk>1238763/title/3573/location/15392368', views.Details, name="details"),
    path('delete/2323<str:pk>2231823/delected/2372332',views.Delete_profile,name="delete"),
    path('delete',views.Delete,name="deletepage"),
    path("cmntsubmit/2563<str:pk>3673672/submit/763567yw2a120",views.cmntsubmit,name="cmntsubmit"),
    path("addwatchlist/4635<str:pk>135790/added/12qw5620",views.addwatchlist,name="addwatchlist"),
    path("removewatchlist/xrt32<str:pk>23weg/remove/6793036wp23",views.removewatchlist,name="removewatchlist"),
    path("watchlist/<str:username>/13r57h/page/1536931390",views.watchlistpage,name="watchlistpage"),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('userss/sd1247<str:pk>37nb_2367s/user/75312793urt34', views.UserName, name="userss"),
    path('aboutus', views.AboutUs, name="aboutus")
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)