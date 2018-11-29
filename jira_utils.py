# Utilities for interacting with Jira

import logging

from jira import JIRA

# create a connection object, jc
#jc = connect_jira("url", "username", "api token")


class JiraClient(object):
    """
    Client to connect to jira
    """

    def __init__(self, server, logger=None):
        self.server = server
        self.logger = logger or logging.getLogger("console")

    def login(self, user, password):
        self.logger.info("Connecting to Jira server {}".format(self.server))

        try:
            self.jira = JIRA(
                options={"server": self.server},
                basic_auth=(user, password),
                verify=False
            )
        except Exception as e:
            self.logger.error("Failed to connect to JIRA.. Error {}".format(
                str(e)))
            exit(1)
        else:
            return True

    def create_issue(self, issue):
        """
        issue requires
        {
          'project': ''
        }
        """
        pass
