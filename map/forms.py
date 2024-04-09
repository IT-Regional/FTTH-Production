from django import forms
from .models import Cluster, Bandeja

class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['name', 'addres', 'lat', 'Ing','c_cluster','tipo','n_bandejas']


class BandejaForm(forms.ModelForm):
    class Meta:
        model = Bandeja
        fields = ['servicio', 'color', 'perdida', 'color_salida', 'servicio_salida']

    def __init__(self, *args, **kwargs):
        self.cluster = kwargs.pop('cluster', None)
        super(BandejaForm, self).__init__(*args, **kwargs)