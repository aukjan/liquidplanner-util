import datetime

from dateutil.rrule import rrule, MO, TU, WE, TH
from dateutil.rrule import DAILY
from dateutil.parser import parse

from liquidplanner import liquidplanner
import settings


__author__ = 'avbelkum'


def timetracking(start, end):
    email = settings.USER
    password = settings.PASS
    LP = liquidplanner(email, password)
    workspace = LP.workspaces()[0]
    LP.set_workspace_id(workspace['id'])
    account = LP.account()
    LP.set_account_id(account['id'])

    meeting_activity_id = 153964
    development_activity_id = 153094
    meeting_task_id = 14905876
    cms_proj_org_id = 14973209

    for date in daterange(start, end):
        assert isinstance(date, datetime.datetime)
        print date.isoformat()
        print LP.track_time(meeting_task_id, meeting_activity_id,
                            date.isoformat(), 3)
        print LP.track_time(cms_proj_org_id, development_activity_id,
                            date.isoformat(), 6)


def daterange(start, end):
    return rrule(DAILY, dtstart=start, until=end, byweekday=(MO, TU, WE, TH))


if __name__ == "__main__":
    s = raw_input("Give start date (d-m-y)  :")
    e = raw_input("Give end date (d-m-y)    :")

    start = parse(str(s))
    end = parse(str(e))
    timetracking(start,end)
