class QuaySigning(object):
    """
    List and manage repository signing information
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, repo):
        return '/api/v1/repository/{repository}/signatures'.format(repository=repo)

    def fetch_all(self, repo):
        """
        Fetches the list of signed tags for the repository.

        GET /api/v1/repository/{repository}/signatures
        """
        url = self._url(repo)
        return self.rest.get(url)
