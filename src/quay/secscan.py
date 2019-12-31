class QuaySecScan(object):
    """
    secscan : List and manage repository vulnerabilities and other security information.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def fetch_manifest_security(self, repo, ref):
        """
        ...

        GET /api/v1/repository/{repository}/manifest/{manifestref}/security

        Parameters:
            vulnerabilities - Include vulnerabilities informations - boolean
        """
        url = '/api/v1/repository/{repository}/manifest/{manifestref}/security'.format(repository=repo, manifestref=ref)
        return self.rest.get(url)

    def fetch_image_security(self, repo, imageid):
        """
        Fetches the features and vulnerabilities (if any) for a repository image.

        GET /api/v1/repository/{repository}/image/{imageid}/security

        Parameters:
            vulnerabilities - Include vulnerabilities informations - boolean
        """
        url = '/api/v1/repository/{repository}/image/{imageid}/security'.format(repository=repo, imageid=imageid)
        return self.rest.get(url)
