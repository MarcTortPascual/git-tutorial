import json 

d={"persona":"marc","edad":"16","lenguages":("phyton","c#")}
ed=open("datos.json","w")
json.dump(d,ed,indent=4)
