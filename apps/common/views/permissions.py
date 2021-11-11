from rest_framework import permissions, status


class AbstractPermission(permissions.BasePermission):

    error_message = None
    error_code = None
    data = None

    def get_message(self):
        return {
            "success": "failed",
            "message": self.error_message,
            "error_code": self.error_code,
            "data": None,
        }

    message = property(get_message)


class IsAuthenticated(AbstractPermission):

    error_code = "AUTHENTICATION_REQUIRED"
    error_message = "Authentication Required"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False


class IsLoggedOut(AbstractPermission):

    error_code = "LOGOUT_REQUIRED"
    error_message = "Please logout to access."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return True
        return False


class UserTypeAccess(AbstractPermission):
    error_code = "USER_ACCESS_REQUIRED"
    error_message = "You are not authorized to perform this action."

    def has_permission(self, request, view):
        if hasattr(request.user, "user_type") and request.user.user_type.user_access_code in view.USER_ACCESS_CODES:
            return True
        return False
