"""Generated client library for servicenetworking version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.servicenetworking.v1alpha import servicenetworking_v1alpha_messages as messages


class ServicenetworkingV1alpha(base_api.BaseApiClient):
  """Generated client library for service servicenetworking version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://servicenetworking.googleapis.com/'

  _PACKAGE = u'servicenetworking'
  _SCOPES = ['https://www.googleapis.com/auth/userinfo.email']
  _VERSION = u'v1alpha'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ServicenetworkingV1alpha'
  _URL_VERSION = u'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new servicenetworking handle."""
    url = url or self.BASE_URL
    super(ServicenetworkingV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)