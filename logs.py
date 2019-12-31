class QuayLogs(object):
    """
    Access usage logs for organizations or repositories.
    """
    def __init__(self, module, rest):
        self.rest = rest
        self.module = module

    def _org_url(self, org):
        return "/api/v1/organization/{orgname}/logs".format(organame=org)

    def _repo_url(self, repo):
        return "/api/v1/repository/{repository}/logs".format(repository=repo)

    def get_org_logs(self, org):
        """
        List the logs for the specified organization.
        
        GET /api/v1/organization/{orgname}/logs

        Parameters:
            next_page - The page token for the next page - string
            performer - Username for which to filter logs - string
            endtime - Latest time for logs. Format: "%m/%d/%Y" in UTC. - string
            starttime - Earliest time for logs. Format: "%m/%d/%Y" in UTC. - string
        """
        response = self.rest.get(self._org_url(org))

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def get_repo_logs(self, repo):
        """
        List the logs for the specified repository.

        GET /api/v1/repository/{repository}/logs

        Parameters:
            next_page - The page token for the next page - string
            endtime - Latest time for logs. Format: "%m/%d/%Y" in UTC. - string
            starttime - Earliest time for logs. Format: "%m/%d/%Y" in UTC. - string
        """
        response = self.rest.get(self._repo_url(repo))

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
    
    def get_user_logs(self, user):
        """
        List the logs for the current user.
        
        GET /api/v1/user/logs

        Parameters:
            next_page - The page token for the next page - string
            performer - Username for which to filter logs. - string
            endtime - Latest time for logs. Format: "%m/%d/%Y" in UTC. - string
            starttime - Earliest time for logs. Format: "%m/%d/%Y" in UTC. - string
        """
        response = self.rest.get('/api/v1/user/logs')

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
