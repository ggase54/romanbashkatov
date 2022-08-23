from rest_framework import serializers
from .models import Checkbox


class CheckboxSerializer(serializers.ModelSerializer):
    # title = serializers.SerializerMethodField()

    class Meta:
        model = Checkbox
        fields = '__all__'


    # @staticmethod
    # def get_title(obj):
    #     return obj.name


class DataSerializer(serializers.Serializer):

    title = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    attrs = serializers.JSONField(required=False)
    type = serializers.CharField(required=False)
    val_1 = serializers.IntegerField()
    val_2 = serializers.IntegerField()

    @staticmethod
    def validate_type(type):
        if not type in ["dict", "list", "tuple"]:
            raise serializers.ValidationError(f"{type} is not allowed")
        return type
