from django.urls import path
from .views import *

# Nombre para la app
app_name = "map"

urlpatterns = [
    path("home/", home_map, name="home"),
    path("cluster/<int:cluster_id>/", cluster_detail, name="cluster_detail"),
    path("home_employee/", home_employee, name="home_employee"),
    path("home_customer", home_customer, name="home_customer"),
    path("logout/", logout_view, name="logout_view"),
    path("add_cluster/", add_cluster, name="add_cluster"),
    path("view_clusters/", view_clusters, name="view_clusters"),
    path(
        "view_clusters/edit_cluster/<int:cluster_id>/",
        edit_cluster,
        name="edit_cluster",
    ),
    path(
        "view_clusters/delete_cluster/<int:cluster_id>/",
        delete_cluster,
        name="delete_cluster",
    ),
    path(
        "view_clusters/view_cluster/<int:cluster_id>/",
        view_cluster,
        name="view_cluster",
    ),
    path(
        "view_clusters/gestionar_bandejas/<int:cluster_id>/",
        gestionar_fusiones,
        name="gestionar_bandejas",
    ),
    path("guardar_ruta/", draw_map, name="guardar_ruta"),
    path("mapa_rutas/", mapa_rutas, name="mapa_rutas"),
    path("mapa_rutas_supervisor/", mapa_rutas_supervisor, name="mapa_rutas_supervisor"),
    path("obtener_rutas/", obtener_rutas, name="obtener_rutas"),
    path("obtener_clusters/", obtener_clusters, name="obtener_clusters"),
    path(
        "view_clusters/editar_fusiones/<int:cluster_id>",
        editar_fusiones,
        name="editar_fusiones",
    ),
    path("view_rutas", view_rutas, name="view_rutas"),
    path("clusters_supervisor", view_clusters_supervisor, name="clusters_supervisor"),
    path("add_cluster_supervisor", add_cluster_supervisor, name="add_cluster_supervisor"),
    path("clusters_supervisor/view_cluster/<int:cluster_id>/", view_cluster_supervidor, name="view_cluster_supervisor"),
    path("clusters_supervisor/delete_cluster/<int:cluster_id>/", delete_cluster_supervisor, name="delete_cluster_supervisor"),
]
