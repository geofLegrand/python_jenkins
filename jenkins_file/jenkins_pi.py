import jenkins
from pprint import pprint

url = "http://3.227.16.75:8080/"

server = jenkins.Jenkins(url, username='devops', password='devops')
#pprint(dir(server))
user = server.get_whoami()
print(server.jobs_count())
jobs = server.get_jobs()

version = server.get_version()
jobs = server.get_jobs()
#pprint(jobs)
jobs = server.get_all_jobs()

for i in server.get_all_jobs():
    if i not in server.get_jobs():
       pprint(i)

#print(jobs)
print('Hello %s from Jenkins %s' % (user['fullName'], version))