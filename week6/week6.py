
import json

#1
dct = {'Tigran': 2, 'Armen': 7, 'Hrant': 4}
print(json.dumps(dct,sort_keys=True,indent=4))


#2
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

js = json.loads(sampleJson)
print(js["company"]["employee"]["payble"]["salary"])


#3

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print(json.dumps(vehicle.__dict__,indent=4))


#4
json_data  = """{
     "name": "Toyota Rav4",
     "engine": "2.5L",
     "price": 32000
}"""

json_reverse = json.loads(json_data)
print(json_reverse)


#5

import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
for x in root.iter():
    print(x.tag,x.attrib)

#6
import xml.etree.ElementTree as ET

tree = ET.parse("movies.xml")
root = tree.getroot()

lst = []
for x in root.iter():
    lst.append(x.tag)
print(lst)

#7
for x in root.findall("./genre/decade/movie/[year='1992']"):
	print(x.attrib) 

#8
for x in root.findall("./genre/decade/movie/format[@multiple='Yes'].."):
	print(x.attrib) 

#9
for movie in root.iter('movie'):
    if movie.get('title') == "Back 2 the Future":
        movie.get('title') =="Back to the Future"
        print (movie.get('title'))

#10
for form in root.findall("./genre/decade/movie/format"):
    if form.attrib['multiple'] == 'False':
        form.set('multiple','No')
tree.write('movies.xml')