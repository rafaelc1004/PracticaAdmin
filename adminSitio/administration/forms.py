from django.forms import ModelForm
from .models import Categoria, Producto

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class ArticuloForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"