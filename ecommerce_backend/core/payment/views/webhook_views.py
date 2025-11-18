import stripe
from django.http import HttpResponse
from django.conf import settings

from core.payment.models.payment import Payment

def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception as e:
        return HttpResponse(status=400)

    # Handle payment success event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        payment_id = session["metadata"]["payment_id"]

        payment = Payment.objects.get(id=payment_id)
        payment.status = "successful"
        payment.save()

    return HttpResponse(status=200)
