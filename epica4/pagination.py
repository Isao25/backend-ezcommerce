from rest_framework.pagination import PageNumberPagination

class CustomArticuloPagination(PageNumberPagination):
    page_query_param = 'page'  # Nombre del parámetro para la página
    page_size_query_param = 'limit'  # Nombre del parámetro para el límite
    page_size = 10  # Valor por defecto si no se especifica 'limit'
    max_page_size = 20  # Límite máximo permitido