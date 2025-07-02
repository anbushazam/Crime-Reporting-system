import os

def get_property_string():
    prop_path=r"C:\Users\AnbuC\PycharmProjects\PythonProject1\util\db.properties"
    with open(prop_path,'r') as f:
        text=f.read()
    lines=text.split('\n')

    credentials=[]
    for line in lines:
        if "="in line:
            property=line.split("=")[1]
            credentials.append(str(property))
    return credentials

