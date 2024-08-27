import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == "POST":
        if 'amount' in request.POST:
            # Step 1: Get the amount from the form and validate it
            try:
                amount = request.POST.get('amount', '0')
                if int(amount) <= 0:
                    raise ValidationError("Amount must be greater than zero.")
                amount_in_paise = int(amount) * 100  # Convert to paise/cents
            except (ValueError, ValidationError) as e:
                return render(request, 'payment.html', {
                    'error': str(e),
                    'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
                })

            # Render the payment page with the amount
            context = {
                'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
                'amount_in_paise': amount_in_paise,
            }
            return render(request, 'payment.html', context)

        elif 'stripeToken' in request.POST:
            # Step 2: Handle the Stripe token and process the payment
            token = request.POST.get('stripeToken')
            amount_in_paise = request.POST.get('amount_in_paise')

            if not amount_in_paise or not amount_in_paise.isdigit() or int(amount_in_paise) <= 0:
                return render(request, 'payment.html', {
                    'error': "Invalid payment amount.",
                    'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
                })

            try:
                charge = stripe.Charge.create(
                    amount=int(amount_in_paise),
                    currency='inr',
                    description='Order payment',
                    source=token,
                )
                return redirect('order_confirm')
            except stripe.error.CardError as e:
                return render(request, 'payment.html', {
                    'error': str(e),
                    'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
                    'amount_in_paise': amount_in_paise
                })

    return render(request, 'payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })


