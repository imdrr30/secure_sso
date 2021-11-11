from .permissions import IsLoggedOut, IsAuthenticated, UserTypeAccess
from .base import BaseAPIView


class LoginRequired(BaseAPIView):
    permission_classes = (IsAuthenticated,)


class LogoutRequired(BaseAPIView):

    permission_classes = (IsLoggedOut,)


class AbstractUserAccessRequired(LoginRequired):
    USER_ACCESS_CODES = None
    permission_classes = (UserTypeAccess,)


class SuperAdminGateWayLoginRequired(AbstractUserAccessRequired):
    USER_ACCESS_CODES = ["SUPERADMIN_GATWAY"]


class AdminGateWayLoginRequired(AbstractUserAccessRequired):
    USER_ACCESS_CODES = ["SUPERADMIN_GATWAY", "ADMIN_GATWAY"]


class SuperAdminOrganizationLoginRequired(AbstractUserAccessRequired):
    USER_ACCESS_CODES = ["SUPERADMIN_ORG"]


class AdminOrganizationLoginRequired(AbstractUserAccessRequired):
    USER_ACCESS_CODES = ["SUPERADMIN_ORG", "ADMIN_ORG"]


class EmployeeOrganizationLoginRequired(AbstractUserAccessRequired):
    USER_ACCESS_CODES = ["SUPERADMIN_ORG", "ADMIN_ORG", "EMP_ORG"]


class EndUserLoginRequired(AbstractUserAccessRequired):
    USER_ACCESS_CODES = ["END_USER"]
