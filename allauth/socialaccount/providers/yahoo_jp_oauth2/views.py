import requests

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)

from .provider import YahooJPOAuth2Provider


class YahooJPOAuth2Adapter(OAuth2Adapter):
    provider_id = YahooJPOAuth2Provider.id
    access_token_url = 'https://auth.login.yahoo.co.jp/yconnect/v1/token'
    authorize_url = 'https://auth.login.yahoo.co.jp/yconnect/v1/authorization'
    profile_url = 'https://userinfo.yahooapis.jp/yconnect/v1/attribute'
    redirect_uri_protocol = 'https'
    use_basic_authorization = True

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token,
                                    'schema': 'openid'})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(YahooJPOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(YahooJPOAuth2Adapter)
