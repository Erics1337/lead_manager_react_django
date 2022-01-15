from rest_framework import serializers
from leads.models import Lead

# Create Serializer from ORM Lead model
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
