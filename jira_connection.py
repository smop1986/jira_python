from jira.client import JIRA
import logging

# Defines a function for connecting to Jira
def connect_jira(log, jira_server, jira_user, jira_password):
    '''
    Connect to JIRA. Return None on error
    '''
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password), verify=False)
                                        # ^--- Note the tuple
        return jira
    except Exception,e:
        log.error("Failed to connect to JIRA: %s" % e)
        return None

# create logger
log = logging.getLogger('devops')

# NOTE: You put your login details in the function call connect_jira(..) below!

# create a connection object, jc
jc = connect_jira(log, "url", "username", "api token")

# print names of all projects
print jc
#projects = jc.projects()
#for v in projects:
 #      print v
