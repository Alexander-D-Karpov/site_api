from rest_framework import routers

from .views import PostSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api', PostSet, basename='auth')

urlpatterns = router.urls