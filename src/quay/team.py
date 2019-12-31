class QuayTeam(object):
    """
    Create, list and manage an organization's teams.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, orgname, teamname, other=None):
        url_str = '/api/v1/organization/{orgname}/team/{teamname}'
        if other is not None:
            url_str += str(other)
        return url_str

    def _(self, orgname, teamname):
        """
        Retrieve the list of members for the specified team.
    
        GET /api/v1/organization/{orgname}/team/{teamname}/members

        Parameters:
            includePending - Whether to include pending members - boolean

        Response:
            200 - Successful invocation
        """
        url = self._url(orgname, teamname, other='/members')
        return self.rest.get(url)

    def _(self, orgname, teamname):
        """
        Returns the list of repository permissions for the org's team.

        GET /api/v1/organization/{orgname}/team/{teamname}/permissions

        Parameters:

        Response:
            200 - Successful invocation
        """
        url = self._url(orgname, teamname, other='/permissions')
        return self.rest.get(url)

    def _(self, orgname, teamname, email):
        """
        Delete an invite of an email address to join a team.

        DELETE /api/v1/organization/{orgname}/team/{teamname}/invite/{email}

        Parameters:

        Response:
            204 - Deleted
        """
        other = '/invite/{email}'.format(email=email)
        url = self._url(orgname, teamname, other)
        return self.rest.delete(url)

    def _(self, orgname, teamname, email):
        """
        Invites an email address to an existing team.

        PUT /api/v1/organization/{orgname}/team/{teamname}/invite/{email}

        Parameters:

        Response:
            200 - Successful invocation
        """
        other = '/invite/{email}'.format(email=email)
        url = self._url(orgname, teamname, other)
        return self.rest.put(url)

    def _(self, orgname, teamname):
        """
        Delete the specified team.

        DELETE /api/v1/organization/{orgname}/team/{teamname}

        Parameters:

        Response:
            204 - Deleted
        """
        url = self._url(orgname, teamname)
        return self.rest.delete(url)

    def _(self, orgname, teamname):
        """
        Update the org-wide permission for the specified team.

        PUT /api/v1/organization/{orgname}/team/{teamname}

        Parameters:
            {
                "role": "member",
                "description": "string"
            }

        Response:
            200 - Successful invocation
        """
        url = self._url(orgname, teamname)
        return self.rest.put(url)

    def _(self, orgname, teamname, membername):
        """
        Delete a member of a team. If the user is merely invited to join the team, then the invite is removed instead.

        DELETE /api/v1/organization/{orgname}/team/{teamname}/members/{membername}

        Parameters:

        Response:
            204 - Deleted
        """
        other = '/members/{membername}'.format(membername=membername)
        url = self._url(orgname, teamname, other)
        return self.rest.delete(url)

    def _(self, orgname, teamname, membername):
        """
        Adds or invites a member to an existing team.

        PUT /api/v1/organization/{orgname}/team/{teamname}/members/{membername}

        Parameters:

        Response:
            200 - Successful invocation
        """
        other = '/members/{membername}'.format(membername=membername)
        url = self._url(orgname, teamname, other)
        return self.rest.put(url)
