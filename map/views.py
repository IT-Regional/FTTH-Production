# Este es el nuevo
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClusterForm, BandejaForm
from .models import Cluster, Ruta, Bandeja
import folium
import branca
from django.contrib.auth import logout
from django.forms import formset_factory, modelformset_factory
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.forms.models import BaseModelFormSet


def home_map(request):
    locations = Cluster.objects.all()
    form = ClusterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("map:home")

    latitud = 13.7942
    longitud = -88.8965

    initialMap = folium.Map(
        location=[latitud, longitud],
        zoom_start=9,
        control_scale=True,
    )
    drawn_items = folium.FeatureGroup()
    initialMap.add_child(drawn_items)

    for idx, location in enumerate(locations, start=1):
        coordinates = (location.lat, location.Ing)
        iframe = branca.element.IFrame(
            html=f"""   
            <h1>{location.tipo} {location.name}</h1><br>
            <strong>Nombre:</strong> {location.name}<br>
            <strong>Latitud:</strong> {location.lat}<br>
            <strong>Longitud:</strong> {location.Ing}<br>
            <strong>Codigo:</strong> {location.c_cluster}<br>
            <strong>Tipo:</strong> {location.tipo}<br>
            <strong>Color de tubo</strong>{location.colors}<br>
            <strong>Numero de Bandejas:</strong> {location.n_bandejas}<br>
            <button onclick="window.open(`/cluster/{location.id}/`)">Ver Información</button>
    """,
            width=500,
            height=250,
        )
        popup = folium.Popup(iframe, max_width=500)
        url = "https://beenet.com.sv/wp-content/images/{}".format
        if location.tipo == "mufa":
            icon_image = url("mufa-removebg-preview.png")
        elif location.tipo == "nap":
            icon_image = url("nap-removebg-preview.png")
        else:
            icon_image = url("cliente-removebg-preview.png")

        icon = folium.CustomIcon(
            icon_image,
            icon_size=(40, 40),
            icon_anchor=(22, 20),
        )
        folium.Marker(coordinates, popup, icon=icon).add_to(initialMap)

        for ruta in Ruta.objects.all():
            geojson_data = json.loads(ruta.geojson_data)
            coordinates_start = geojson_data["geometry"]["coordinates"][0]
            coordinates_end = geojson_data["geometry"]["coordinates"][-1]
            layer = folium.GeoJson(geojson_data, name=ruta.nombre)
            folium.GeoJson(geojson_data).add_to(drawn_items)
            popup_html = (
                f"<b>Nombre de la ruta: {ruta.nombre}</b><br>"
                f"<b>Coordenadas de Inicio:</b> {coordinates_start}</br>"
                f"<b>Coordenadas de fin:</b> {coordinates_end}</br>"
            )
            layer.add_child(folium.Popup(popup_html, max_width=300))
            layer.add_to(drawn_items)

    # Añadir control de capas (Layers Control)
    """ folium.LayerControl().add_to(initialMap) """

    context = {"map": initialMap._repr_html_(), "locations": locations, "form": form}
    return render(request, "home.html", context)


def cluster_detail(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    context = {"cluster", cluster}
    return render(request, "cluster_detail.html", context)

def home_customer(request):
    locations = Cluster.objects.all()
    form = ClusterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("map:home")

    latitud = 13.7942
    longitud = -88.8965

    initialMap = folium.Map(
        location=[latitud, longitud],
        zoom_start=9,
        control_scale=True,
    )
    drawn_items = folium.FeatureGroup()
    initialMap.add_child(drawn_items)

    for idx, location in enumerate(locations, start=1):
        coordinates = (location.lat, location.Ing)
        iframe = branca.element.IFrame(
            html=f"""   
            <h1>{location.tipo} {location.name}</h1><br>
            <strong>Nombre:</strong> {location.name}<br>
            <strong>Latitud:</strong> {location.lat}<br>
            <strong>Longitud:</strong> {location.Ing}<br>
            <strong>Codigo:</strong> {location.c_cluster}<br>
            <strong>Tipo:</strong> {location.tipo}<br>
            <strong>Color de tubo</strong>{location.colors}<br>
            <strong>Numero de Bandejas:</strong> {location.n_bandejas}<br>
            <button onclick="window.open(`/cluster/{location.id}/`)">Ver Información</button>
    """,
            width=500,
            height=250,
        )
        popup = folium.Popup(iframe, max_width=500)
        url = "https://beenet.com.sv/wp-content/images/{}".format
        if location.tipo == "mufa":
            icon_image = url("mufa-removebg-preview.png")
        elif location.tipo == "nap":
            icon_image = url("nap-removebg-preview.png")
        else:
            icon_image = url("cliente-removebg-preview.png")

        icon = folium.CustomIcon(
            icon_image,
            icon_size=(40, 40),
            icon_anchor=(22, 20),
        )
        folium.Marker(coordinates, popup, icon=icon).add_to(initialMap)

        for ruta in Ruta.objects.all():
            geojson_data = json.loads(ruta.geojson_data)
            coordinates_start = geojson_data["geometry"]["coordinates"][0]
            coordinates_end = geojson_data["geometry"]["coordinates"][-1]
            layer = folium.GeoJson(geojson_data, name=ruta.nombre)
            folium.GeoJson(geojson_data).add_to(drawn_items)
            popup_html = (
                f"<b>Nombre de la ruta: {ruta.nombre}</b><br>"
                f"<b>Coordenadas de Inicio:</b> {coordinates_start}</br>"
                f"<b>Coordenadas de fin:</b> {coordinates_end}</br>"
            )
            layer.add_child(folium.Popup(popup_html, max_width=300))
            layer.add_to(drawn_items)

    # Añadir control de capas (Layers Control)
    """ folium.LayerControl().add_to(initialMap) """

    context = {"map": initialMap._repr_html_(), "locations": locations, "form": form}
    return render(request, "home_customer.html", context)


def home_employee(request):
    locations = Cluster.objects.all()
    form = ClusterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("map:home")

    latitud = 13.7942
    longitud = -88.8965

    initialMap = folium.Map(
        location=[latitud, longitud],
        zoom_start=9,
        control_scale=True,
    )
    drawn_items = folium.FeatureGroup()
    initialMap.add_child(drawn_items)

    for idx, location in enumerate(locations, start=1):
        coordinates = (location.lat, location.Ing)
        iframe = branca.element.IFrame(
            html=f"""   
            <h1>{location.tipo} {location.name}</h1><br>
            <strong>Nombre:</strong> {location.name}<br>
            <strong>Latitud:</strong> {location.lat}<br>
            <strong>Longitud:</strong> {location.Ing}<br>
            <strong>Codigo:</strong> {location.c_cluster}<br>
            <strong>Tipo:</strong> {location.tipo}<br>
            <strong>Color de tubo</strong>{location.colors}<br>
            <strong>Numero de Bandejas:</strong> {location.n_bandejas}<br>
            <button onclick="window.open(`/cluster/{location.id}/`)">Ver Información</button>
    """,
            width=500,
            height=250,
        )
        popup = folium.Popup(iframe, max_width=500)
        url = "https://beenet.com.sv/wp-content/images/{}".format
        if location.tipo == "mufa":
            icon_image = url("mufa-removebg-preview.png")
        elif location.tipo == "nap":
            icon_image = url("nap-removebg-preview.png")
        else:
            icon_image = url("cliente-removebg-preview.png")

        icon = folium.CustomIcon(
            icon_image,
            icon_size=(40, 40),
            icon_anchor=(22, 20),
        )
        folium.Marker(coordinates, popup, icon=icon).add_to(initialMap)

        for ruta in Ruta.objects.all():
            geojson_data = json.loads(ruta.geojson_data)
            coordinates_start = geojson_data["geometry"]["coordinates"][0]
            coordinates_end = geojson_data["geometry"]["coordinates"][-1]
            layer = folium.GeoJson(geojson_data, name=ruta.nombre)
            folium.GeoJson(geojson_data).add_to(drawn_items)
            popup_html = (
                f"<b>Nombre de la ruta: {ruta.nombre}</b><br>"
                f"<b>Coordenadas de Inicio:</b> {coordinates_start}</br>"
                f"<b>Coordenadas de fin:</b> {coordinates_end}</br>"
            )
            layer.add_child(folium.Popup(popup_html, max_width=300))
            layer.add_to(drawn_items)

    # Añadir control de capas (Layers Control)
    """ folium.LayerControl().add_to(initialMap) """

    context = {"map": initialMap._repr_html_(), "locations": locations, "form": form}
    return render(request, "employee.html", context)


def add_cluster(request):
    cluster_instance = Cluster()
    context = {
        "Cluster": cluster_instance,
    }
    return render(request, "add_cluster.html", context)

def add_cluster_supervisor(request):
    cluster_instance = Cluster()
    context = {"Cluster" : cluster_instance}

    return render(request, "add_cluster_supervisor.html",context)


def view_clusters(request):
    location = Cluster.objects.all()
    context = {"locations": location}
    return render(request, "view_clusters.html", context)

def view_clusters_supervisor(request):
    location = Cluster.objects.all()
    context = {"locations" : location}
    return render(request, "view_clusters_supervisor.html", context)


def edit_cluster(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)
    form = ClusterForm(request.POST or None, instance=cluster)

    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("map:view_clusters")

    context = {"form": form, "cluster": cluster}
    return render(request, "edit_cluster.html", context)


def delete_cluster(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)

    if request.method == "POST":
        cluster.delete()
        return redirect("map:view_clusters")

    context = {"cluster": cluster}
    return render(request, "delete_cluster.html", context)

def delete_cluster_supervisor(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)

    if request.method == "POST":
        cluster.delete()
        return redirect("map:clusters_supervisor")
    
    context = {"cluster" : cluster}

    return render(request, "delete_cluster_supervisor.html", context)


def logout_view(request):
    logout(request)

    return redirect("new_login.html")


def view_cluster(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)
    context = {"cluster": cluster}

    return render(request, "view_cluster.html", context)

def view_cluster_supervidor(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)
    context = {"cluster" : cluster}

    return render(request, "view_cluster_supervisor.html", context)


def gestionar_bandejas(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    BandejaFormSet = formset_factory(Bandeja, extra=cluster.n_bandejas)

    if request.method == "POST":
        formset = BandejaFormSet(request.POST, prefix="bandejas")

        if formset.is_valid():
            # Procesar los datos del formset
            for form in formset:
                # Acceder a los datos de cada formulario
                nombre = form.cleaned_data["nombre"]
                """ descripcion = form.cleaned_data['descripcion'] """
                # Realizar operaciones con los datos (guardar en la base de datos, por ejemplo)

            # Redirigir a la página que desees después de procesar los datos
            return redirect("map:view_clusters")

    else:
        formset = BandejaFormSet(prefix="bandejas")

    context = {"formset": formset, "cluster_id": cluster_id}
    return render(request, "gestionar_bandejas.html", context)


@csrf_exempt
def draw_map(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            nombre_ruta = data.get("nombre", "")
            geojson_data = json.dumps(data.get("geojson", {}))
            color_ruta = data.get("color", "blue")
            comentario = data.get("comentario", "")

            Ruta.objects.create(
                nombre=nombre_ruta, geojson_data=geojson_data, color=color_ruta,comentario=comentario
            )

            return JsonResponse({"status": "OK"})
        except Exception as e:
            return JsonResponse({"status": "Error", "message": str(e)})

    return JsonResponse(
        {"status": "Error", "message": "Solo se admiten solicitudes POST"}
    )


def mapa_rutas(request):
    rutas = Ruta.objects.all()
    context = {
        "rutas": rutas,
    }
    return render(request, "dibujo.html", context)


def draw_map_supervisor(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            nombre_ruta = data.get("nombre", "")
            geojson_data = json.dumps(data.get("geojson", {}))
            color_ruta = data.get("color", "blue")
            comentario = data.get("comentario", "")

            Ruta.objects.create(
                nombre=nombre_ruta, geojson_data=geojson_data, color=color_ruta,comentario=comentario
            )

            return JsonResponse({"status": "OK"})
        except Exception as e:
            return JsonResponse({"status": "Error", "message": str(e)})

    return JsonResponse(
        {"status": "Error", "message": "Solo se admiten solicitudes POST"}
    )

def mapa_rutas_supervisor(request):
    rutas = Ruta.objects.all()
    context = {
        "rutas": rutas,
    }
    return render(request, "dibujo_supervisor.html", context)

def obtener_rutas(request):
    rutas = Ruta.objects.all()
    features = []

    for ruta in rutas:
        features.append(
            {
                "type": "Feature",
                "properties": {"nombre": ruta.nombre},
                "geometry": json.loads(ruta.geojson_data),
            }
        )

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return JsonResponse(geojson, safe=False)


def pintar_rutas(request):

    return render(request, "pintar_rutas.html")


def obtener_clusters(request):
    clusters = Cluster.objects.all()
    cluster_data = []

    for cluster in clusters:
        if cluster.lat is not None and cluster.Ing is not None:
            cluster_data.append(
                {
                    "name": cluster.name,
                    "lat": cluster.lat,
                    "Ing": cluster.Ing,
                    "tipo": cluster.tipo,
                    "n_bandejas": cluster.n_bandejas,
                }
            )

    return JsonResponse({"clusters": cluster_data})


def gestionar_fusiones(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)

    BandejaFormSet = modelformset_factory(
        Bandeja, form=BandejaForm, extra=cluster.n_fusiones, formset=BaseModelFormSet
    )

    if request.method == "POST":
        formset = BandejaFormSet(
            request.POST,
            prefix="fusiones",
            queryset=Bandeja.objects.filter(cluster=cluster),
        )

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.cluster = cluster
                instance.save()

            return redirect("map:view_clusters")
    else:
        formset = BandejaFormSet(
            queryset=Bandeja.objects.filter(cluster=cluster), prefix="fusiones"
        )

    context = {"formset": formset, "cluster_id": cluster_id}
    return render(request, "gestionar_bandejas.html", context)


def editar_fusiones(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    BandejaFormSet = modelformset_factory(
        Bandeja, form=BandejaForm, extra=0, formset=BaseModelFormSet
    )

    if request.method == "POST":
        formset = BandejaFormSet(
            request.POST,
            prefix="fusiones",
            queryset=Bandeja.objects.filter(cluster=cluster),
        )
        if formset.is_valid():
            formset.save()
            return redirect(
                "map:view_clusters"
            )  # Redirigir a la página deseada después de guardar
    else:
        formset = BandejaFormSet(
            queryset=Bandeja.objects.filter(cluster=cluster), prefix="fusiones"
        )

    context = {"formset": formset, "cluster_id": cluster_id}
    return render(request, "mostrar_fusiones.html", context)


def view_rutas(request):
    ruta = Ruta.objects.all()
    context = {"ruta": ruta}

    return render(request, "view_rutas.html", context)
