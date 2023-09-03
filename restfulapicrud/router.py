from empregadoapi.viewsets import EmpregadoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empregado',EmpregadoViewset)



