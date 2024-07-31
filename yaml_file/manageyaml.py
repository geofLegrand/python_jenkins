import yaml



def red_yaml_file(yaml_file):
    _yaml_file = {}
    try:
        with open(yaml_file,'r') as yaml_doc:
            _yaml_file = yaml.load(yaml_doc) #,Loader=yaml.FullLoader
        return _yaml_file
    except Exception as e:

        print("Erreur",e)



def write_yaml_file(file_save,_yaml_file):
    try:
        with open(file_save,'w') as yaml_doc:
            g = yaml.dump(_yaml_file)
            yaml_doc.write(g)
            print("file save successfully !")
    except Exception as e:

        print("Erreur",e)




if __name__=="__main__":
    red_yaml_file("my.yaml")