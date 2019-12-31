class QuayManifest(object):
    """
    Manage the manifests of a repository.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _manifest_url(self, repo, manifestref, labelid=None):
        url_str = '/api/v1/repository/{repository}/manifest/{manifestref}'
        if labelid is not None:
            url_str += '/labels' + str(labelid)
        return url_str

    def fetch_all_manifest(self, repo, manifestref):
        """
        ...

        GET /api/v1/repository/{repository}/manifest/{manifestref}

        """
        url = self._manifest_url(repo, manifestref)
        response = self.rest.get(url)
        
        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_all_labels(self,repo, manifestref):
        """
        ...

        GET /api/v1/repository/{repository}/manifest/{manifestref}/labels

        Parameters:
            filter - If specified, only labels matching the given prefix will be returned - string

        """
        url = self._manifest_url(repo, manifestref, '')
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def add_label(self, repo, manifestref, data):
        """
        Adds a new label into the tag manifest.

        POST /api/v1/repository/{repository}/manifest/{manifestref}/labels

        Parameters:
            {
                "media_type": "text/plain",
                "value": "string",
                "key": "string"
            }

        """
        url = self._manifest_url(repo, manifestref, '')
        response = self.rest.post(url, data)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def get_label(self, repo, manifestref, labelid):
        """
        Retrieves the label with the specific ID under the manifest.

        GET /api/v1/repository/{repository}/manifest/{manifestref}/labels/{labelid}

        """
        url = self._manifest_url(repo, manifestref, labelid)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete_label(self, repo, manifestref, labelid):
        """
        Deletes an existing label from a manifest.

        DELETE /api/v1/repository/{repository}/manifest/{manifestref}/labels/{labelid}

        """
        url = self._manifest_url(repo, manifestref, labelid)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info
