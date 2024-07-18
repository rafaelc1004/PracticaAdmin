

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = "__all__"