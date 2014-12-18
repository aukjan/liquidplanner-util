from dateutil.rrule import rrule, MO, TU, WE, TH
from dateutil.rrule import DAILY
from liquidplanner import liquidplanner
import settings

__author__ = 'avbelkum'


def timetracking():
    email = settings.USER
    password = settings.PASS
    LP = liquidplanner(email, password)
    workspace = LP.workspaces()[0]
    LP.set_workspace_id(workspace['id'])
    account = LP.account()
    LP.set_account_id(account['id'])

    # Get all Timesheets for a project
    # print LP.project_timesheets(19319793)

    # Print a single timesheet
    print LP.timesheet(809907)

    # Get all projects and print them
    projects = LP.projects()
    for proj in projects:
        print "({}) {}".format(proj['id'], proj['name'])

    meeting_activity_id = 153964
    development_activity_id = 153094
    meeting_task_id = 14905876
    cms_proj_org_id = 14973209

    # start=datetime.datetime(2014, 4, 11)
    # end=datetime.datetime(2014, 6, 1)
    # for timesheet in LP.timesheets():
    # print timesheet
    #
    #
    # for date in daterange(start,end):
    # assert isinstance(date, datetime.datetime)
    #     print date.isoformat()
    #     print LP.track_time(meeting_task_id,meeting_activity_id,date.isoformat(),3)
    #     print LP.track_time(cms_proj_org_id,development_activity_id,date.isoformat(),6)


def daterange(start, end):
    return rrule(DAILY, dtstart=start, until=end, byweekday=(MO, TU, WE, TH))


if __name__ == "__main__":
    timetracking()
