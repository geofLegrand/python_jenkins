import sys
#import json
from pprint import pprint
import yaml
#from apis import jen
#from csv_file import csvgeneretor as c
from yaml_file import manageyaml as y


print(sys.platform)
def data_jenkins():
    file_name = "jenkins_jobs.csv"
    header = ['Job_name', 'Job_url', 'Job_color']
    keys=['name','color','url']
    content = jen.my_jobs(keys)
    c.csv_generator(file_name,header,content)


def update_yaml_file(_file,save_file):
    json_file = y.red_yaml_file(_file)
    pprint(json_file)
    if json_file:     
        json_file['spec']['ports'][0]['nodePort']= 31200
        json_file['spec']['ports'][0]['port']= 9600
        y.write_yaml_file(save_file,json_file)



if __name__=="__main__":
    update_yaml_file("my.yaml","my01.yaml")