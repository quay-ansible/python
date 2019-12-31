class QuayGlobalMessages(object):
    """
    Messages API
    """
    def __init__(self, module, rest):
        self.rest = rest
        self.module = module

    def fetch_all(self):
        """
        Return a super users messages
        
        GET /api/v1/messages
        """
        url = "/api/v1/messages"
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def create(self, body):
        """
        Create a message
        
        POST /api/v1/messages

        Parameters:
            {
                "message": {
                    "content": "string",
                    "media_type": "text/plain",
                    "severity": "info"
                }
            }
        """
        url = "/api/v1/messages"
        response = self.rest.post(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info
