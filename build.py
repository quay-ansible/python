class QuayBuild(object):
    """
    Create, list, cancel and get status/logs of repository builds.
    """
    def __init__(self, module, rest):
        self.rest = rest
        self.module = module
    
    def _build_url(self, repo, uuid=None, other=None):
        url_str = "/api/v1/repository/" + str(repo) +"/build/"
        if uuid is not None:
            url_str += str(uuid)
        if other is not None:
            url_str += '/' + str(other)
        return url_str

    def list_builds(self, repo):
        """
        Get the list of repository builds.

        GET /api/v1/repository/{repository}/build/

        Parameters:
            since - Returns all builds since the given unix timecode - integer
            limit - The maximum number of builds to response = - integer
        """
        url = self._build_url(repo)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def build_request(self, repo, body):
        """
        Request that a repository be built and pushed from the specified input.

        POST /api/v1/repository/{repository}/build/

        Parameters:
            {
                "subdirectory": "string",
                "archive_url": "string",
                "docker_tags": [
                "string"
                ],
                "pull_robot": "string",
                "file_id": "string",
                "context": "string",
                "dockerfile_path": "string"
            }
        """
        url = self._build_url(repo)
        response = self.rest.post(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def build_status(self, repo, uuid):
        """
        Return the status for the builds specified by the build uuids.

        GET /api/v1/repository/{repository}/build/{build_uuid}/status
        """
        url = self._build_url(repo, uuid, other='status')
        response = self.rest.get(url)
    
        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def cancel_build(self, repo, uuid):
        """
        Cancels a repository build.
        
        DELETE /api/v1/repository/{repository}/build/{build_uuid}
        """
        url = self._build_url(repo, uuid)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def build_info(self, repo, uuid):
        """
        Returns information about a build.
        
        GET /api/v1/repository/{repository}/build/{build_uuid}
        """
        url = self._build_url(repo, uuid)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def build_logs(self, repo, uuid):
        """
        Return the build logs for the build specified by the build uuid.
        
        GET /api/v1/repository/{repository}/build/{build_uuid}/logs 
        """
        url = self._build_url(repo, uuid, other='logs')
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
