# json
import json

dictData = {'name':'tom', 'age':33,'score':[90, 80, 100]}
print(dictData, type(dict))

str_val = json.dumps(dictData)
print(str_val, type(str_val))
print(str_val[0:10])


json_val = json.loads(str_val)
print(json_val, type(json_val))

# dict type이므로 슬라이싱이 안됨
# print(json_val[0:10]) # TypeError : unhashable type : 'slice'

print(json_val['name'])
print(json_val['score'])

print()
for k in json_val.keys():
    print(k)

for v in json_val.values():
    print(v)
    
print()
name_data = json_val.get('name')
print(name_data)
    
    
