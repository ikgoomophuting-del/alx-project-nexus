from rest_framework import serializers
from core.payment.models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'reference', 'status', 'created_at']

