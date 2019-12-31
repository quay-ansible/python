class QuayUser(object):
    """
    Manage the current user.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def fetch_auth_user_info(self):
        """
        Get user information for the authenticated user.

        GET /api/v1/user/

        Response:
            {
                "organizations": [
                    {}
                ],
                "verified": true,
                "avatar": {},
                "anonymous": true,
                "logins": [
                    {}
                ],
                "can_create_repo": true,
                "preferred_namespace": true,
                "email": "string"
            }
        """
        url = '/api/v1/user/'
        return self.rest.get(url)

    def fetch_user_info(self, user):
        """
        Get user information for the specified user.

        GET /api/v1/users/{username}

        """
        url = '/api/v1/users/{username}'.format(username=user)
        return self.rest.get(url)

    def list_all_starred(self):
        """
        List all starred repositories.

        GET /api/v1/user/starred

        Parameters:
            next_page - The page token for the next page - string
        """
        url = '/api/v1/user/starred'
        return self.rest.get(url)

    def add_star(self, body):
        """
        Star a repository.

        POST /api/v1/user/starred

        Parameters:
            {
                "namespace": "string",
                "repository": "string"
            }
        """
        url = '/api/v1/user/starred'
        return self.rest.post(url, data=body)

    def remove_star(self, repo):
        """
        Removes a star from a repository.

        DELETE /api/v1/user/starred/{repository}

        """
        url = '/api/v1/user/starred/{repository}'.format(repository=repo)
        return self.rest.delete(url)
