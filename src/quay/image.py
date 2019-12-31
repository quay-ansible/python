class QuayImage(object):
    """
    List and lookup repository images
    """
    def __init__(self, module, rest):
        self.rest = rest
        self.module = module

    def _img_url(self, repo, image_id=None):
        url_str = "/api/v1/repository/" + str(repo) + "/image/"
        if repo is not None:
            url_str += str(image_id)
        return url_str

    def list_images(self, repo):
        """
        List the images for the specified repository.

        GET /api/v1/repository/{repository}/image/
        
        Parameters:
        """
        url = self._img_url(repo)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info


    def get_info(self, repo, image_id):
        """
        Get the information available for the specified image.

        GET /api/v1/repository/{repository}/image/{image_id}

        Parameters:
        """
        url = self._img_url(repo, image_id)
        response = self.rest.get(url)

        if response.status_code is not 200:
            self.module.fail_json(msg=response.json)
        return response.info
