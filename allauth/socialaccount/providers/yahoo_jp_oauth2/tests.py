# -*- coding: utf-8 -*-

from allauth.socialaccount.tests import create_oauth2_tests
from allauth.tests import MockedResponse
from allauth.socialaccount.providers import registry

from .provider import YahooJPOAuth2Provider

class YahooJPOAuth2Tests(create_oauth2_tests(registry.by_id(YahooJPOAuth2Provider.id))):
    def get_mocked_response(self):
        return MockedResponse(200, """
{
  "user_id": "43M63NAGMHBAYMXRMY3WODOWS4",
  "name": "矢風太郎",
  "given_name": "太郎",
  "given_name#ja-Kana-JP": "タロウ",
  "given_name#ja-Hani-JP": "太郎",
  "family_name": "矢風",
  "family_name#ja-Kana-JP": "ヤフウ",
  "family_name#ja-Hani-JP": "矢風",
  "gender": "male",
  "birthday": "2000",
  "locale": "ja-JP",
  "email": "your_email@example.com",
  "email_verified": true,
  "address": {
    "locality": "港区",
    "region": "東京都",
    "postal_code": "1076211",
    "country": "jp"
  }
}""")
