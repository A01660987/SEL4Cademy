from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from SEL4C.views import GenderViewSet, CountryViewSet, UserViewSet, AdministratorViewSet, GroupViewSet, InstitutionViewSet, AcademicDegreeViewSet, AcademicDegreeOfferViewSet, AcademicDisciplineViewSet, StudentViewSet, DiagnosisQuestionViewSet, TestViewSet, ImplementationProcessViewSet, CompetenceDiagnosisViewSet, DiagnosisTestViewSet, CompetenceViewSet, ResourceViewSet, TrainingReagentViewSet, TrainingActivityViewSet
from SEL4C.views import activity, diagnosis, credentials

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register(r'gender', GenderViewSet)
router.register(r'country', CountryViewSet)
router.register(r'user', UserViewSet)
router.register(r'administrator', AdministratorViewSet)
router.register(r'group', GroupViewSet)
router.register(r'institution', InstitutionViewSet)
router.register(r'academic-degree', AcademicDegreeViewSet)
router.register(r'academic-degree-offer', AcademicDegreeOfferViewSet)
router.register(r'academic-discipline', AcademicDisciplineViewSet)
router.register(r'student', StudentViewSet)
router.register(r'diagnosis-question', DiagnosisQuestionViewSet)
router.register(r'test', TestViewSet)
router.register(r'implementation-process', ImplementationProcessViewSet)
router.register(r'competence-diagnosis', CompetenceDiagnosisViewSet)
router.register(r'diagnosis-test', DiagnosisTestViewSet)
router.register(r'competence', CompetenceViewSet)
router.register(r'resource', ResourceViewSet)
router.register(r'training-reagent', TrainingReagentViewSet)
router.register(r'training-activity', TrainingActivityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/schema/', SpectacularAPIView.as_view(api_version='v2'), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view()), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'), 
    path('api/', include(router.urls)), 
    path('api/activity', activity, name="api/activity"), 
    path('api/diagnosis', diagnosis, name="api/diagnosis"), 
    path('api/credentials', credentials, name="api/credentials"), 
    path('', include('web.urls'))
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
