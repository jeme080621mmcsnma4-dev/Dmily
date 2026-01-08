from django.urls import path
from .views import ( lisAllEmpleados,
ListByAreaEmpleado,
ListEmpleadoByKword,
ListHabilidadesEmpleados,
EmpleadoDetailView,                    
EmpleadoCreateView,
SuccessView, EmpleadoUpdateView,EmpleadoDeleteView,InicioView, ListaEmpleadosAdmin,

)

app_name='persona_app'

urlpatterns = [
    path('', InicioView.as_view()),
    path('listar-todos-empleados/', lisAllEmpleados.as_view()),
    path('buscar-empleado/', ListEmpleadoByKword.as_view()),
    path('lista-habilidades-empleado/', ListHabilidadesEmpleados.as_view()),
    path(
    'ver-empleado/<pk>/',
    EmpleadoDetailView.as_view(),
    name='empleado_detail'
),

    path('add-empleado/', 
        EmpleadoCreateView.as_view(),
        name='empleado_add'),
    path(
        'success/',
        SuccessView.as_view(),
        name='correcto'),
    path(
        'update-empleado/<pk>/',
        EmpleadoUpdateView.as_view(),
        name='modificar_empleado'),
    path(
        'delate-empleado/<pk>/',
        EmpleadoDeleteView.as_view(),
        name='Eliminar_empleado'),
    path(
        'ver-empleado/<pk>/',
        EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),

    path(
        'list-by-area/<subnombre>/',
        ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),

    path(
        'lista-empleados-admin/',
        ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
]

