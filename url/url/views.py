from django.http import Http404
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import UrlShortener
from .forms import UrlShortenerForm
import shortuuid

def generate_unique_short_code():
    return shortuuid.uuid()[:8]

def shorten_url(request):
    if request.method == 'POST':
        form = UrlShortenerForm(request.POST)
        if form.is_valid():
            url_shortener = form.save(commit=False)
            while True:
                try:
                    url_shortener.short_code = generate_unique_short_code()
                    url_shortener.save()
                    break
                except IntegrityError:
                    # The short_code already exists, generate a new one and try again
                    pass
            return render(request, 'shortened.html', {'url_shortener': url_shortener})
    else:
        form = UrlShortenerForm()
    return render(request, 'shorten_url.html', {'form': form})

def redirect_to_original(request, short_code):
    try:
        url_shortener = UrlShortener.objects.get(short_code=short_code)
        return redirect(url_shortener.long_url)
    except UrlShortener.DoesNotExist:
        raise Http404("Shortened URL does not exist")
