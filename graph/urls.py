from django.urls import path
from .views import index  , GraphViewSet , NodeViewSet , EdgeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'graphs' , GraphViewSet)
router.register(r'nodes' , NodeViewSet)
router.register(r'edges' , EdgeViewSet)


urlpatterns = router.urls
urlpatterns += [path("helloworld/", index)]
