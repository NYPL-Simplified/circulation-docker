import json
from pdb import set_trace

class GitHubEventParser(object):

    MASTER_BRANCH_TAG = 'development'

    @classmethod
    def get_tag(cls, response):
        
