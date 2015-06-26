from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import YahooJPOAuth2Provider

urlpatterns = default_urlpatterns(YahooJPOAuth2Provider)
