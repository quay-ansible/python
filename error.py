class QuayError(object):
    """
    Error details API
    """
    def __init__(self, module, rest):
        self.rest = rest
        self.module = module

    def _error_url(self, error=None):
        url_str = "/api/v1/error"
        if error is not None:
            url_str += '/' + str(error)
        return url_str

    def get_error(self, error):
        """
        Get a detailed description of the error

        GET /api/v1/error/{error_type}

        Response:
            {
                "type": "string",
                "description": "string",
                "title": "downstream_issue"
            }
        """
        url = self._error_url(error)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
