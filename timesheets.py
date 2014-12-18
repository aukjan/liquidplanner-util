import datetime
import getpass

__author__ = 'avbelkum'
import requests
import json
from dateutil.rrule import DAILY, rrule, MO, TU, WE, TH


class LiquidPlanner():
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


    def track_time(self, task_id, act_id, day, hours):
        return json.loads(self.post('/workspaces/' + str(self.workspace_id) +
                                    '/tasks/' + str(task_id) + '/track_time',
                                    json.dumps({'work': hours,
                                                'activity_id': act_id,
                                                'work_performed_on': day
                                    })).content)

    @staticmethod
    def timetracking():
        email = raw_input(prompt="Email please: ")
        password = getpass.getpass(prompt="Password: ")
        LP = LiquidPlanner(email, password)
        workspace = LP.workspaces()[0]
        LP.set_workspace_id(workspace['id'])
        account = LP.account()
        LP.set_account_id(account['id'])

        meeting_activity_id = 153964
        development_activity_id = 153094
        meeting_task_id = 14905876
        cms_proj_org_id = 14973209

        start=datetime.datetime(2014, 4, 11)
        end=datetime.datetime(2014, 6, 1)
        for timesheet in LP.timesheets():
            print timesheet


        for date in daterange(start,end):
            assert isinstance(date, datetime.datetime)
            print date.isoformat()
            print LP.track_time(meeting_task_id,meeting_activity_id,date.isoformat(),3)
            print LP.track_time(cms_proj_org_id,development_activity_id,date.isoformat(),6)


def daterange(start, end):
    return rrule(DAILY, dtstart=start, until=end, byweekday=(MO, TU, WE, TH))


if __name__ == "__main__":
    LiquidPlanner.timetracking()


