from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class BaseModelViewSet(ModelViewSet):
    action_type = None
    model_data = None

    def get_user_access_codes(self):
        return {}

    @staticmethod
    def wrap_success_response(response, message, error_code=None):
        data = {
            "status": "success",
            "message": message,
            "error_code": error_code,
            "data": response.data,
        }
        response.data = data
        return response

    def get_model(self):
        return self.model_data

    def get_user_access_type(self):
        return self.request.user.user_type.user_access_code

    def get_queryset(self):
        return self.get_user_access_codes()[self.get_user_access_type()][
            "queryset"
        ].filter(is_deleted=False)

    def create(self, request, *args, **kwargs):
        self.action_type = "create"
        response = super().create(request, *args, **kwargs)

        return self.wrap_success_response(
            response, f"{self.get_model().__name__} created successfully."
        )

    def update(self, request, *args, **kwargs):
        self.action_type = "update"

        response = super().update(request, *args, **kwargs)
        return self.wrap_success_response(
            response, f"{self.get_model().__name__} update successfully."
        )

    def retrieve(self, request, *args, **kwargs):
        self.action_type = "detail"
        response = super().retrieve(request, *args, **kwargs)

        return self.wrap_success_response(
            response, f"{self.get_model().__name__} retrieved successfully."
        )

    def list(self, request, *args, **kwargs):
        self.action_type = "list"

        response = super().list(request, *args, **kwargs)
        return self.wrap_success_response(
            response, f"{self.get_model().__name__} listed successfully."
        )

    def destroy(self, request, *args, **kwargs):
        self.action_type = "delete"
        obj = self.get_object()
        obj.is_deleted = True
        obj.save()
        return Response(
            data={
                "status": "success",
                "message": f"{obj.id} is deleted.",
                "error_code": None,
                "data": None,
            }
        )

    def get_action_type(self):
        return self.action_type

    def get_serializer_class(self):
        meta_class_fields = self.get_user_access_codes()[self.get_user_access_type()][
            "common_meta"
        ]

        serializers_extra_fields = self.get_user_access_codes()[
            self.get_user_access_type()
        ].get("extra_fields", {})

        if self.get_action_type() in self.get_user_access_codes()[
            self.get_user_access_type()
        ].keys() and isinstance(
            self.get_user_access_codes()[self.get_user_access_type()][
                self.get_action_type()
            ],
            dict,
        ):
            meta_class_fields.update(
                self.get_user_access_codes()[self.get_user_access_type()][
                    self.get_action_type()
                ]
            )

        class BaseSerializer(serializers.ModelSerializer):
            class Meta:
                model = self.get_model()
                fields = meta_class_fields["fields"]

        serializer = BaseSerializer

        for field, data in meta_class_fields.items():
            setattr(serializer.Meta, field, data)

        for field, data in serializers_extra_fields.items():
            setattr(serializer, field, data)

        return serializer
