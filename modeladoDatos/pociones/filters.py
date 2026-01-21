import django_filters

from pociones.models import Pocion


class PocionFilter(django_filters.FilterSet):
    precio_min = django_filters.NumberFilter(
        field_name='precio',
        lookup_expr='gte'
    )
    precio_max = django_filters.NumberFilter(
        field_name='precio',
        lookup_expr='lte'
    )
    nombre = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Pocion
        fields = ['nombre', 'precio', 'tamano', 'ingredientes']