from rest_framework import permissions
from apps.configurations.viewsets import METHOD_TO_ACTION_TYPE


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
        user_access_codes = view.get_user_access_codes()

        possible_actions = METHOD_TO_ACTION_TYPE.get(request.method, False)

        if not possible_actions:
            return False

        if (
            hasattr(request.user, "user_type")
            and view.get_user_access_type() in user_access_codes.keys()
        ):
            action_flag = False

            allowed_actions = user_access_codes[view.get_user_access_type()][
                "operations"
            ].keys()
            for action in possible_actions:
                if action in allowed_actions:
                    action_flag = True
                    break
            return action_flag
        return False
