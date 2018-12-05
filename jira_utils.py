# Utilities for interacting with Jira

from jira import JIRA


class JiraClient(object):
    """
    Client to connect to jira
    """

    def __init__(self, server, logger=None):
        self.server = server

    def login(self, user, password):
        print("Connecting to Jira server {}".format(self.server))
        try:
            self.jira = JIRA(
                options={"server": self.server,
                         "verify": False},
                basic_auth=(user, password),
            )
        except Exception as e:
            print("Failed to connect to JIRA.. Error {}".format(
                str(e)))
            exit(1)
        else:
            return True

    def create_issue(self, **kwargs):
        """
        issue requires
        {
          'project': ''
        }
        """
        return self.jira.create_issue(**kwargs)
