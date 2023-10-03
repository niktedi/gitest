import sys
import numpy
import os
import ftrack_api as ft
for key in os.environ.keys():
    pass
    #print(key +"=" + os.environ[key])
ses = ft.Session(server_url='https://krab.ftrackapp.com',api_key='YWJhNjkzMGItMDU2Zi00MzQ3LTk0M2EtNjQwYWFkYjcxYTMwOjo1ZWU1NzYwZi01NjkxLTQ2YmUtYThjOS0wODY4ZGM0MjA0YjI',api_user='robox@tut.by')

asset=ses.query('Asset where name is "nasos"').first()
print(asset['versions'][0]['components'][2]['component_locations'][0]['location']['id'])
