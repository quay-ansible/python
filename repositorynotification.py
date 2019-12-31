class QuayRepositoryNotification(object):
    """
    List, create and manage repository events/notifications.
    """
    def __init__(self, module, rest):
        self.module = module
        self.rest = rest

    def _url(self, repo, uuid=None):
        url_str = '/api/v1/repository/{repository}/notification/'.format(repository=repo)
        if uuid is not None:
            url_str += str(uuid)
        return url_str

    def test(self, repo, uuid):
        """
        Queues a test notification for this repository.

        POST /api/v1/repository/{repository}/notification/{uuid}/test
        """
        url = self._url(repo, uuid)
        response = self.rest.post(url + '/test')

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def delete(self, repo, uuid):
        """
        Deletes the specified notification.

        DELETE /api/v1/repository/{repository}/notification/{uuid}
        """
        url = self._url(repo, uuid)
        response = self.rest.delete(url)

        if response.status_code is not 204:
            self.module.fail_json(msg=response.json)
        return response.info

    def fetch_info(self, repo, uuid):
        """
        Get information for the specified notification.

        GET /api/v1/repository/{repository}/notification/{uuid}
        """
        url = self._url(repo, uuid)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def reset(self, repo, uuid):
        """
        Resets repository notification to 0 failures.

        POST /api/v1/repository/{repository}/notification/{uuid}
        """
        url = self._url(repo, uuid)
        response = self.rest.post(url)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info

    def list_all(self, repo):
        """
        List the notifications for the specified repository.

        GET /api/v1/repository/{repository}/notification/
        """
        url = self._url(repo)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info

    def create(self, repo, body):
        """
        ...

        POST /api/v1/repository/{repository}/notification/

        Parameters:
            {
                "eventConfig": {},
                "title": "string",
                "config": {},
                "event": "string",
                "method": "string"
            }
        """
        url = self._url(repo)
        response = self.rest.post(url, data=body)

        if response.status_code is not 201:
            self.module.fail_json(msg=response.json)
        return response.info
