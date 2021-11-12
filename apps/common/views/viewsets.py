from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    action_type = None
    model_data = None

    def get_user_access_codes(self):
        return {}

    def get_model(self):
        return self.model_data

    def get_user_access_type(self):
        return self.request.user.user_type.user_access_code

    def get_queryset(self):
        return self.get_user_access_codes()[self.get_user_access_type()]["queryset"]

    def create(self, request, *args, **kwargs):
        self.action_type = "create"
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.action_type = "update"
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.action_type = "detail"
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.action_type = "list"
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.action_type = "delete"
        return super().destroy(request, *args, **kwargs)

    def get_action_type(self):
        return self.action_type

    def get_serializer_class(self):
        meta_class_fields = self.get_user_access_codes()[self.get_user_access_type()][
            "common_meta"
        ]

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

        return serializer
