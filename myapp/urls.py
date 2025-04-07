from django.urls import path
from . import views



urlpatterns = [
    # Core routes
    path('', views.dashboard, name='dashboard'),
    
    # Authentication routes
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Application routes
    
    path('services/', views.services, name='services'),
    path('tools/', views.Tool, name='tools'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources_view, name='resources'),
    path('trade/', views.trade, name='trade'),
    path('privacy/', views.privacy, name='privacy'),
    path('TandC/', views.TandC, name='TandC'),
    path('FAQs/', views.FAQs, name='FAQs'),
    
    # Polygon-related routes
    path('add_polygon/', views.add_polygon, name='add_polygon'),
    path('polygons/', views.polygon_list, name='polygon_list'),
    path('agro_data/<str:polygon_id>/', views.get_agro_data, name='get_agro_data'),
    path('details/<str:polygon_id>/', views.details, name='details'),
    
    # Additional features
     path("detect/", views.detect_disease, name="detect_disease"),
    path('news/', views.news, name='news'),
    path("plant-health/", views.detect_disease, name="plant_health"),
    path("plant-health/", views.detect_disease, name="plant_disease_detection"),
    path('plant-health/results/', views.plant_health_results, name='plant_health_results'),
    path('plant-health/download/', views.download_report, name='download_report'),
    path("plant-health/results/delete/<str:timestamp>/", views.delete_report, name="delete_report"),
]
