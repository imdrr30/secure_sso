from rest_framework.permissions import BasePermission


class IsEndUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type.user_access_code == "END_USER"


class IsOrganization(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type.user_access_code in [
            "SUPERADMIN_ORG",
            "ADMIN_ORG",
            "EMP_ORG",
        ]
