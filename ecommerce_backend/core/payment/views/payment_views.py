import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.payment.models.payment import Payment

class CreateStripeCheckoutSession(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get("amount")    # must be Decimal
        cart_id = request.data.get("cart_id")  # optional
        user = request.user

        if not amount:
            return Response({"error": "Amount is required"}, status=400)

        # Stripe requires amount in cents
        stripe_amount = int(float(amount) * 100)

        # Create Payment record (pending)
        payment = Payment.objects.create(
            user=user,
            amount=amount,
            reference=f"pay_{user.id}_{payment_id:=4}",
            status="pending"
        )

        # Create Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': stripe_amount,
                        'product_data': {
                            'name': f"Order for {user.username}"
                        }
                    },
                    'quantity': 1
                }
            ],
            mode="payment",
            success_url=f"{settings.DOMAIN_URL}/payments/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{settings.DOMAIN_URL}/payments/cancel",
            metadata={"payment_id": payment.id}
        )

        return Response({"checkout_url": session.url})

