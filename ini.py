import sys
import numpy
import os
import ftrack_api as ft
for key in os.environ.keys():
    print(key +"=" + os.environ[key])
ses = ft.Session(server_url='https://krab.ftrackapp.com',api_key='YWJhNjkzMGItMDU2Zi00MzQ3LTk0M2EtNjQwYWFkYjcxYTMwOjo1ZWU1NzYwZi01NjkxLTQ2YmUtYThjOS0wODY4ZGM0MjA0YjI',api_user='robox@tut.by')
user = ses.query('User').first()
with ses.auto_populating(False):  # For demonstration purpose only.
    print(user.items())