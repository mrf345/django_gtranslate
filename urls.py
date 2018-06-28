from django.urls import include, path


urlpatterns = [
    path('gtran/', include('gtranslate.urls')),
    path('gtran_auth/', include('gtranslate.urls_auth'))
]