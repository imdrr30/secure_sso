from .permissions import IsLoggedOut, IsAuthenticated, UserTypeAccess
from .base import BaseAPIView


class LoginRequired(BaseAPIView):
    permission_classes = (IsAuthenticated,)


class LogoutRequired(BaseAPIView):

    permission_classes = (IsLoggedOut,)


class AbstractUserAccessRequired(LoginRequired):
    USER_ACCESS_CODES = None
    permission_classes = (UserTypeAccess,)