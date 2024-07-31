import jenkins
import csv
import os 


def authentication():
    
    jenkins_url='http://3.227.16.75:8080'
    jenkins_username='devops'
    jenkins_pass='devops'
    #print(os.environ)
    # os.environ['jenkins_url'] , os.environ['jenkins_username'] ,os.environ['jenkins_pass']
    server = jenkins.Jenkins(jenkins_url,jenkins_username,jenkins_pass)
    # number_jobs=server.jobs_count()
    # user = server.get_whoami()['fullName']
    return server



def my_jobs(keys:[]) -> list:
    try:
        server = authentication()
        _jobs = server.get_all_jobs()
        return [ [ job.get(key) for key in keys ] for job in _jobs ]

    except Exception as e:
        print("Error !!!!", e)

        

if __name__ =='__main__':
    print(__name__)
