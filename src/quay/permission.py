class QuayPermission(object):
    """
    Manage repository permissions.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, repo, other=None):
        url_str = '/api/v1/repository/{repository}/permissions'.format(repository=repo)
        if other is not None:
            url_str += str(other)
        return url_str

    def delete_team_permission(self, repo, team):
        """
        Delete the permission for the specified team.

        DELETE /api/v1/repository/{repository}/permissions/team/{teamname}
        """
        other = '/team/{teamname}'.format(teamname=team)
        url = self._url(repo, other)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_team_permission(self, repo, team):
        """
        Fetch the permission for the specified team.
        
        GET /api/v1/repository/{repository}/permissions/team/{teamname}
        """
        other = '/team/{teamname}'.format(teamname=team)
        url = self._url(repo, other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def update_team_permission(self, repo, team, body):
        """
        Update the existing team permission.

        PUT /api/v1/repository/{repository}/permissions/team/{teamname}

        Parameters:
            {
                "role": "read"
            }
        """
        other = '/team/{teamname}'.format(teamname=team)
        url = self._url(repo, other)
        response = self.rest.put(url, data=body)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def list_user_permissions(self, repo):
        """
        List all user permissions.

        GET /api/v1/repository/{repository}/permissions/user/
        """
        other = '/user/'
        url = self._url(repo, other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def list_team_permission(self, repo):
        """
        List all team permission.

        GET /api/v1/repository/{repository}/permissions/team/
        """
        other = '/team/'
        url = self._url(repo, other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete_user_permissions(self, repo, username):
        """
        Delete the permission for the user.

        DELETE /api/v1/repository/{repository}/permissions/user/{username}
        """
        other = '/user/{username}'.format(username=username)
        url = self._url(repo, other)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_user_permissions(self, repo, username):
        """
        Get the permission for the specified user.
        
        GET /api/v1/repository/{repository}/permissions/user/{username}
        """
        other = '/user/{username}'.format(username=username)
        url = self._url(repo, other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def update_user_permissions(self, repo, username, body):
        """
        Update the perimssions for an existing repository.
        
        PUT /api/v1/repository/{repository}/permissions/user/{username}

        Parameters:
            {
                "role": "read"
            }
        """
        other = '/user/{username}'.format(username=username)
        url = self._url(repo, other)
        response = self.rest.put(url, data=body)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_transitive_permission(self, repo, username):
        """
        Get the fetch the permission for the specified user.
        
        GET /api/v1/repository/{repository}/permissions/user/{username}/transitive
        """
        other = '/user/{username}/transitive'.format(username=username)
        url = self._url(repo, other)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
