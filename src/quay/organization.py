class QuayOrganization(object):
    """
    Manage organizations, members and OAuth applications.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, orgname, other=None):
        url_str = '/api/v1/organization/{orgname}'.format(orgname)
        if other is not None:
            url_str = str(other)
        return url_str

    def fetch_app_info(self, client):
        """
        Get information on the specified application.

        GET /api/v1/app/{client_id}
        """
        url = '/api/v1/app/{client_id}'.format(client_id=client)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def create_org(self, body):
        """
        Create a new organization.

        POST /api/v1/organization/

        Parameters:
            {
                "recaptcha_response":   "string",
                "name":                 "string",
                "email":                "string"
            }
        """
        url = self._url('')
        response = self.rest.post(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete_org(self, orgname):
        """
        Deletes the specified organization.
        
        DELETE /api/v1/organization/{orgname}
        """
        url = self._url(orgname)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_org(self, orgname):
        """
        Get the details for the specified organization
        
        GET /api/v1/organization/{orgname}
        """
        url = self._url(orgname)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def modify_org(self, orgname, body):
        """
        Change the details for the specified organization.

        PUT /api/v1/organization/{orgname}

        Parameters:
            {
                "invoice_email":    true,
                "email":            "string",
                "tag_expiration_s": 0
            }
        """
        url = self._url(orgname)
        response = self.rest.put(url, data=body)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def list_collaborators(self, orgname):
        """
        List outside collaborators of the specified organization.

        GET /api/v1/organization/{orgname}/collaborators
        """
        other = '/collaborators'
        url = self._url(orgname, other=other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def list_all_apps(self, orgname):
        """
        List the applications for the specified organization

        GET /api/v1/organization/{orgname}/applications
        """
        other = '/applications'
        url = self._url(orgname, other=other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def create_app(self, orgname, body):
        """
        Creates a new application under this organization.

        POST /api/v1/organization/{orgname}/applications

        Parameters:
            {
                "redirect_uri":     "string",
                "avatar_email":     "string",
                "name":             "string",
                "application_uri":  "string",
                "description":      "string"
            }
        """
        other = '/applications'
        url = self._url(orgname, other=other)
        response = self.rest.post(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete_app(self, orgname, client_id):
        """
        Deletes the application under this organization.

        DELETE /api/v1/organization/{orgname}/applications/{client_id}
        """
        other = '/applications/{client_id}'.format(client_id=client_id)
        url = self._url(orgname, other=other)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_app(self, orgname, client_id):
        """
        Retrieves the application with the specified client_id under the specified organization

        GET /api/v1/organization/{orgname}/applications/{client_id}
        """
        other = '/applications/{client_id}'.format(client_id=client_id)
        url = self._url(orgname, other=other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def update_app(self, orgname, client_id, body):
        """
        Updates an application under this organization.

        PUT /api/v1/organization/{orgname}/applications/{client_id}

        Parameters:
            {
                "redirect_uri":     "string",
                "avatar_email":     "string",
                "name":             "string",
                "application_uri":  "string",
                "description":      "string"
            }
        """
        other = '/applications/{client_id}'.format(client_id=client_id)
        url = self._url(orgname, other=other)
        response = self.rest.put(url, data=body)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def list_members(self, orgname):
        """
        List the human members of the specified organization.

        GET /api/v1/organization/{orgname}/members
        """
        other = '/members'
        url = self._url(orgname, other=other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete_member(self, orgname, membername):
        """
        Removes a member from an organization, revoking all its repository priviledges and removing
        it from all teams in the organization.

        DELETE /api/v1/organization/{orgname}/members/{membername}
        """
        other = '/members/{membername}'.format(membername=membername)
        url = self._url(orgname, other=other)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_member(self, orgname, membername):
        """
        Retrieves the details of a member of the organization.

        GET /api/v1/organization/{orgname}/members/{membername}
        """
        other = '/members/{membername}'.format(membername=membername)
        url = self._url(orgname, other=other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
