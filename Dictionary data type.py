Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> iccpoints={'india':125,'eng':105,'aus':97,'NZL':97}
>>> iccpoints
{'india': 125, 'eng': 105, 'aus': 97, 'NZL': 97}
>>> iccpoints.get('india')
125
>>> iccpoints['india']=130
>>> iccpoints
{'india': 130, 'eng': 105, 'aus': 97, 'NZL': 97}
>>> iccpoints['pak']=70
>>> iccpoints
{'india': 130, 'eng': 105, 'aus': 97, 'NZL': 97, 'pak': 70}
>>> points={'p1':[10,10,'monu','prabhat'],'p2':[20,20]}
>>> points.get('pi')
>>> points.get('pi')
>>> points.get('p1')
[10, 10, 'monu', 'prabhat']
>>> number={'n1':(10,10),'n2':[20,20]}
>>> count={"p1":[10,10],'p1':[20,20]}
>>> count.get("p1")
[20, 20]
>>> masoom={2:"rollno.",826:"regno"}
>>> masoom.get(2)
'rollno.'
>>> ali={(2,'mass','ali'):20,}
>>> ali.get((2,'mass','ali'))
20
>>> modify={['list']=20}
SyntaxError: invalid syntax
>>> modify={['list']:20}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    modify={['list']:20}
TypeError: unhashable type: 'list'
>>> #list cant be use as key
>>> dict={len(['love']):'priya'}
dict.get(len(['love']))






