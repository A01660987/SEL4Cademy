from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, authentication, permissions
from SEL4C.serializers import *
from SEL4C.models import *


@extend_schema_view(
    list=extend_schema(description="Get a list"),
    retrieve=extend_schema(description="Get an item"),
    create=extend_schema(description="Create an item"),
    update=extend_schema(description="Update an item"),
    destroy=extend_schema(description="Delete an item"),
)

# Permissions
def permission_get(self):
    if self.request.method == "GET":
        return [permissions.IsAuthenticated()]
    else:
        return [permissions.IsAdminUser()]


authentication_methods = [
    authentication.SessionAuthentication,
    authentication.TokenAuthentication,
]


class GenderViewSet(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = authentication_methods
    # TODO


class AdministratorViewSet(viewsets.ModelViewSet):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
    authentication_classes = authentication_methods
    # TODO


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    authentication_classes = authentication_methods
    # TODO


class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class AcademicDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDegreeSerializer
    queryset = AcademicDegree.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class AcademicDegreeOfferViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDegreeOfferSerializer
    queryset = AcademicDegreeOffer.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class AcademicDisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicDisciplineSerializer
    queryset = AcademicDiscipline.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = authentication_methods
    # TODO


class DiagnosisQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisQuestionSerializer
    queryset = DiagnosisQuestion.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class ImplementationProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ImplementationProcessSerializer
    queryset = ImplementationProcess.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class CompetenceDiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceDiagnosisSerializer
    queryset = CompetenceDiagnosis.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class DiagnosisTestViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisTestSerializer
    queryset = DiagnosisTest.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class CompetenceViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class TrainingReagentViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingReagentSerializer
    queryset = TrainingReagent.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get


class TrainingActivityViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingActivitySerializer
    queryset = TrainingActivity.objects.all()
    authentication_classes = authentication_methods
    get_permissions = permission_get
