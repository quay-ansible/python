class QuayPrototype(object):
    """
    Manage default permissions added to repositories.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, orgname, other=None):
        url_str = '/api/v1/organization/{orgname}/prototypes'.format(orgname=orgname)
        if other is not None:
            url_str += str(other)
        return url_str

    def list_existing(self, orgname):
        """
        List the existing prototypes for this organization.
        
        GET /api/v1/organization/{orgname}/prototypes
        """
        url = self._url(orgname)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def create_permission(self, orgname, body):
        """
        Create a new permission prototype.

        POST /api/v1/organization/{orgname}/prototypes

        Parameters:
            {
                "activating_user": {
                    "name": "string"
                },
                "role": "read",
                "delegate": {
                    "kind": "user",
                    "name": "string"
                }
            }
        """
        url = self._url(orgname)
        response = self.rest.post(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete_permission(self, orgname, prototypeid):
        """
        Delete an existing permission prototype.

        DELETE /api/v1/organization/{orgname}/prototypes/{prototypeid}
        """
        other = '/{prototypeid}'.format(prototypeid=prototypeid)
        url = self._url(orgname, other)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def update_role(self, orgname, prototypeid, body):
        """
        Update the role of an existing permission prototype.

        PUT /api/v1/organization/{orgname}/prototypes/{prototypeid}

        Parameters:
            {
                "role": "read"
            }
        """
        other = '/{prototypeid}'.format(prototypeid=prototypeid)
        url = self._url(orgname, other)
        response = self.rest.put(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info
