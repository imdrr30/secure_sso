from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    def get_user_access_codes(self):
        return {}

    def get_queryset(self):
        return self.get_user_access_codes()[
            self.request.user.user_type.user_access_code
        ]["queryset"]
