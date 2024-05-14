from rest_framework import serializers
from .models import*

class superAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = superAdmin
        fields = '__all__'

class adminSerializer(serializers.ModelSerializer):
    # superadmin = superAdminSerialzier(read_only = True)
    class Meta:
        model = admin
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    # admin = adminSerialzier(read_only = True)
    class Meta:
        model = user
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    # user = userSerialzier(read_only = True)
    class Meta:
        model = product
        fields = '__all__'