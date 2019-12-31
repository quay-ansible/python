class QuayTrigger(object):
    """
    Create, list and manage build triggers.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, repo, uuid=None, other=None):
        url_str = '/api/v1/repository/{repository}/trigger/'.format(repository=repo)
        if uuid is not None:
            url_str += str(uuid)
        if other is not None:
            url_str += str(other)
        return url_str
    
    def _(self, repo):
        """
        List the triggers for the specified repository.
        
        GET /api/v1/repository/{repository}/trigger/

        Response Messages:
            200 - Successful invocation
	
        """
        url = self._url(repo)
        return self.rest.get(url)

    def _(self, repo, uuid, body):
        """
        Activate the specified build trigger.

        post /api/v1/repository/{repository}/trigger/{trigger_uuid}/activate

        Parameters:
            {
                "pull_robot": "string",
                "config": {}
            }

        Response Messages:
            201 - Successful creation

        """
        url = self._url(repo, uuid, other='/activate')
        return self.rest.post(url, data=body)

    def _(self, repo, uuid, body):
        """
        Manually start a build from the specified trigger.

        post /api/v1/repository/{repository}/trigger/{trigger_uuid}/start

        Parameters:
            {
                "branch_name": "string",
                "commit_sha": "string"
            }

        Response Messages:
            201 - Successful creation

        """
        url = self._url(repo, uuid, other='/start')
        return self.rest.post(url, data=body)

    def _(self, repo, uuid):
        """
        List the builds started by the specified trigger.
        
        get /api/v1/repository/{repository}/trigger/{trigger_uuid}/builds
        
        Parameters:
            limit - The maximum number of builds to return - integer
        
        Response Messages:
            200 - Successful invocation

        """
        url = self._url(repo, uuid, other='/builds')
        return self.rest.get(url)

    def _(self, repo, uuid):
        """
        Delete the specified build trigger.

        delete /api/v1/repository/{repository}/trigger/{trigger_uuid}

        Parameters:
        
        Response Messages:
            204 - Deleted

        """
        url = self._url(repo, uuid)
        return self.rest.delete(url)

    def _(self, repo, uuid):
        """
        Get information for the specified build trigger.

        get /api/v1/repository/{repository}/trigger/{trigger_uuid}
        
        Parameters:
        
        Response Messages:
            200 - Successful invocation

        """
        url = self._url(repo, uuid)
        return self.rest.get(url)

    def _(self, repo, uuid, body):
        """
        Updates the specified build trigger.

        put /api/v1/repository/{repository}/trigger/{trigger_uuid}

        Parameters:
            {
                "enabled": true
            }

        Response Messages:
            200 - Successful invocation

        """
        url = self._url(repo, uuid)
        return self.rest.put(url, data=body)
