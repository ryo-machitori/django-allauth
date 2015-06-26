from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class YahooJPOAuth2Account(ProviderAccount):

    def to_str(self):
        dflt = super(YahooJPOAuth2Account, self).to_str()
        return self.account.extra_data.get('name', dflt)


class YahooJPOAuth2Provider(OAuth2Provider):
    id = 'yahoo_jp_oauth2'
    name = 'YahooJPOAuth2'
    package = 'allauth.socialaccount.providers.yahoo_jp_oauth2'
    account_class = YahooJPOAuth2Account

    def extract_uid(self, data):
        return data.get('user_id')

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    first_name=data.get('given_name'),
                    last_name=data.get('family_name'))


providers.registry.register(YahooJPOAuth2Provider)
