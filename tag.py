class QuayTag(object):
    """
    Manage the tags of a repository.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest
        
    def _url(self, repo, tag=None, other=None):
        url_str = '/api/v1/repository/{repository}/tag/'.format(repository=repo)
        if tag is not None:
            url_str += str(tag)
        if other is not None:
            url_str += str(other)
        return url_str

    def _(self, repo, tag):
        """
        List the images for the specified repository tag.

        GET /api/v1/repository/{repository}/tag/{tag}/images

        Parameters:
            owned - If specified, only images wholely owned by this tag are returned - boolean
        """
        url = self._url(repo, tag, '/images')
        return self.rest.get(url)

    def _(self, repo, tag, body):
        """
        Restores a repository tag back to a previous image in the repository.

        POST /api/v1/repository/{repository}/tag/{tag}/restore

        Parameters:
            {
                "image": "string",
                "manifest_digest": "string"
            }
        """
        url = self._url(repo, tag, '/restore')
        return self.rest.post(url, data=body)

    def _(self, repo, tag):
        """
        Delete the specified repository tag.

        DELETE /api/v1/repository/{repository}/tag/{tag}
        """
        url = self._url(repo, tag)
        return self.rest.delete(url)

    def _(self, repo, tag, body='{}'):
        """
        Change which image a tag points to or create a new tag.

        PUT /api/v1/repository/{repository}/tag/{tag}

        Parameters:
            {}
        """
        url = self._url(repo, tag)
        return self.rest.put(url, data=body)

    def fetch_all(self, repo):
        """
        get /api/v1/repository/{repository}/tag/

        Parameters:
            onlyActiveTags - Filter to only active tags - boolean
            page - Page index for the results. Default 1 - integer
            limit - Limit to the number of results to return per page. Max 100 - integer
            specificTag - Filters the tags to the specific tag - string
        """
        url = self._url(repo)
        return self.rest.get(url)
