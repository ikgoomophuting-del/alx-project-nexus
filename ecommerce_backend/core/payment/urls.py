from django.urls import path
from core.payment.views.payment_views import CreateStripeCheckoutSession
from core.payment.views.webhook_views import stripe_webhook

urlpatterns = [
    path('create/', CreateStripeCheckoutSession.as_view(), name="create-payment"),
    path('webhook/', stripe_webhook, name="stripe-webhook"),
]
