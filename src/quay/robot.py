class QuayRobot(object):
    """
    Manage user and organization robot accounts.
    """
    def __init__(self, module, rest):
        self.rest = rest
        self.base_path_org = "/api/v1/organization"
        self.base_path_user= "/api/v1/user/robots"
        self.module = module
        self.connection = None

    def _org_url(self, orgname, robot_shortname=None, other=None):
        if orgname is None:
            self.module.fail_json(msg="Organization undefined")
        url_str = self.base_path_org + '/' + orgname + '/robots'
        if robot_shortname is not None:
            url_str += '/' + str(robot_shortname)
        if other is not None:
            url_str += '/' + str(other)
        return url_str

    def _user_url(self, robot_shortname=None, other=None):
        url_str = self.base_path_user
        if robot_shortname is not None:
            url_str += '/' + robot_shortname
        if other is not None:
            url_str += '/' + other
        return url_str

    def list_all_robots(self):
        """
        List the available robots for the user.

        GET /api/v1/user/robots

        Parameters:
            limit - If specified, the number of robots to return. - integer
            token - If false, the robot's token is not returned. - boolean
            permissions - Whether to include repositories and teams in which the robots have permission. - boolean
        """
        url = self._user_url()
        return self.rest.get(url)

    def fetch1_permissions(self, robot):
        """
        Returns the list of repository permissions for the user's robot.

        GET /api/v1/user/robots/{robot_shortname}/permissions
        """
        other = '/permissions'
        url = self._user_url(robot, other)
        return self.rest.put(url)

    def regenerate_token(self, robot):
        """
        Regenerates the token for a user's robot.

        POST /api/v1/user/robots/{robot_shortname}/regenerate
        """
        other = '/regenerate'
        url = self._user_url(robot, other)
        return self.rest.post(url)

    def delete_robot(self, robot):
        """
        Delete an existing robot.

        DELETE /api/v1/user/robots/{robot_shortname}
        """
        url = self._user_url(robot)
        return self.rest.delete(url)

    def fetch_robot(self, robot):
        """
        Returns the user's robot with the specified name.

        GET /api/v1/user/robots/{robot_shortname}
        """
        url = self._user_url(robot)
        return self.rest.get(url)

    def create_robot(self, robot, body):
        """
        Create a new user robot with the specified name.

        PUT /api/v1/user/robots/{robot_shortname}

        Parameters:
            {
                "unstructured_metadata": {},
                "description": "string"
            }
        """
        url = self._user_url(robot)
        return self.rest.put(url, data=body)

    def fetch_org_permsissions(self, orgname, robot):
        """
        Returns the list of repository permissions for the org's robot.

        GET /api/v1/organization/{orgname}/robots/{robot_shortname}/permissions
        """
        other = '/permissions'
        url = self._org_url(orgname, robot, other)
        return self.rest.get(url)

    def regenerate_org_token(self, orgname, robot):
        """
        Regenerates the token for an organization robot.

        POST /api/v1/organization/{orgname}/robots/{robot_shortname}/regenerate
        """
        other = '/regenerate'
        url = self._org_url(orgname, robot, other)
        return self.rest.post(url)

    def list_all_org_robots(self, orgname):
        """
        List the organization's robots.

        GET /api/v1/organization/{orgname}/robots

        Parameters:
            limit - If specified, the number of robots to return. - integer
            token - If false, the robot's token is not returned. - boolean
            permissions - Whether to include repostories and teams in which the robots have permission. - boolean

        """
        url = self._org_url(orgname)
        return self.rest.get(url)

    def delete_org_robot(self, orgname, robot):
        """
        Delete an existing organization robot.

        DELETE /api/v1/organization/{orgname}/robots/{robot_shortname}
        """
        url = self._org_url(orgname, robot)
        return self.rest.delete(url)

    def fetch_org_robot(self, orgname, robot):
        """
        Returns the organization's robot with the specified name.

        GET /api/v1/organization/{orgname}/robots/{robot_shortname}
        """
        url = self._org_url(orgname, robot)
        return self.rest.get(url)

    def create_org_robot(self, orgname, robot, body):
        """
        Create a new robot in the organization.

        PUT /api/v1/organization/{orgname}/robots/{robot_shortname}

        Parameters:
            {
                "unstructured_metadata": {},
                "description": "string"
            }
        """
        url = self._org_url(orgname, robot)
        return self.rest.put(url, data=body)
