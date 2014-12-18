__author__ = 'avbelkum'
import json
import requests


class liquidplanner():
    base_uri = 'https://app.liquidplanner.com/api'
    workspace_id = None
    email = None
    password = None
    session = None
    account_id = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_workspace_id(self):
        return self.workspace_id

    def set_workspace_id(self, workspace_id):
        self.workspace_id = workspace_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get(self, uri, options={}):
        return requests.get(self.base_uri + uri,
                            data=options,
                            headers={'Content-Type': 'application/json'},
                            auth=(self.email, self.password)
        )

    def post(self, uri, options={}):
        return requests.post(self.base_uri + uri,
                             data=options,
                             headers={'Content-Type': 'application/json'},
                             auth=(self.email, self.password)
        )

    def put(self, uri, options={}):
        return requests.put(self.base_uri + uri,
                            data=options,
                            headers={'Content-Type': 'application/json'},
                            auth=(self.email, self.password)
        )

    def account(self):
        return json.loads(self.get('/account').content)

    def workspaces(self):
        return json.loads(self.get('/workspaces').content)

    def projects(self):
        return json.loads(self.get('/workspaces/' + str(self.workspace_id) +
                                   '/projects').content)

    def tasks(self):
        return json.loads(self.get('/workspaces/' + str(self.workspace_id) +
                                   '/tasks').content)

    def create_task(self, data):
        return json.loads(self.post('/workspaces/' + str(self.workspace_id) +
                                    '/tasks',
                                    json.dumps({'task': data})).content)

    def update_task(self, data):
        return json.loads(self.put('/workspaces/' + str(self.workspace_id) +
                                   '/tasks/' + str(data['id']),
                                   json.dumps({'task': data})).content)

    def timesheets(self):
        return json.loads(self.get('/workspaces/' + str(self.workspace_id) +
                                   '/timesheets?member_id=' + str(
            self.account_id)).content)

    def timesheet(self, sheet_id):
        return json.loads(self.get('/workspaces/' + str(self.workspace_id) +
                                   '/timesheets/' + str(sheet_id)).content)

    def project_timesheets(self, project_id):
        return json.loads(self.get('/workspaces/' + str(self.workspace_id) +
                                   '/timesheets?project_id=' + str(
            project_id)).content)

    def track_time(self, task_id, act_id, day, hours):
        return json.loads(self.post('/workspaces/' + str(self.workspace_id) +
                                    '/tasks/' + str(task_id) + '/track_time',
                                    json.dumps({'work': hours,
                                                'activity_id': act_id,
                                                'work_performed_on': day
                                    })).content)




