class QuaySearch(object):
    """
    Conduct searches against all registry context.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def find(self):
        """
        Get a list of entities and resources that match the specified query.

        GET /api/v1/find/all

        Parameters:
            query - The search query - string 
        """
        url = '/api/v1/find/all'
        return self.rest.get(url)

    def find_repo(self):
        """
        Get a list of apps and repositories that match the specified query.

        GET /api/v1/find/repositories

        Parameters:
            query - The search query - string 
        """
        url = '/api/v1/find/repositories'
        return self.rest.get(url)

    def find_prefix(self, prefix):
        """
        Get a list of entities that match the specified prefix.

        GET /api/v1/entities/{prefix}

        Parameters:
            includeOrgs  - Whether to include orgs names - boolean
            includeTeams - Whether to include team names - boolean
            namespace    - Namespace to use when querying for org entities - string
        """
        url = '/api/v1/entities/{prefix}'.format(prefix=prefix)
        return self.rest.get(url)
