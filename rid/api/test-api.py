from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from auth.models import RidUser


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RidUser
        fields = ('rid', 'first_name','last_name', 'is_staff')

# ViewSets define the view behavior.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = RidUser.objects.all()
    def get_queryset(self):
	   return RidUser.objects.filter(rid=self.request.user.rid)
    

router = routers.DefaultRouter()
router.register(r'university_info', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
