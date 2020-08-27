Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=3+4j
>>> b=2+3j
>>> print(b-a)
(-1-1j)
>>> a=6+4j
>>> b=3+2j
>>> c=a*b
>>> print(c)
(10+24j)
>>> a=6+4j
>>> b=3+2j
>>> print(a*b)
(10+24j)
>>> print(a/b)
(2+0j)
>>> 5*2**10
5120
>>> \a
SyntaxError: unexpected character after line continuation character
>>> print(\a)
SyntaxError: unexpected character after line continuation character
>>> print('\a')

>>> name='masoom'
>>> name2='ali'
>>> print('my first name is %s and my second name is %s.'%(name,name2))
my first name is masoom and my second name is ali.
>>> 'my first name is %s'%(name, )
'my first name is masoom'
>>> 'my second name is'%(name2,)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'my second name is'%(name2,)
TypeError: not all arguments converted during string formatting
>>> 'my second name is %s'%(name2,)
'my second name is ali'
>>> 'my second name is %s'%(name2)
'my second name is ali'
>>> my second name is %s %(name2)
SyntaxError: invalid syntax
>>> print('my second name is %s'%(name2))
my second name is ali
>>> a=1234
>>> b='hey'
>>> 'hello priya say masoom to %s and send the code %u '%(b,a)
'hello priya say masoom to hey and send the code 1234 '
>>> 'hello priya say masoom to %s and send the code %i'%(b,a)
'hello priya say masoom to hey and send the code 1234'
>>> a=+$512
SyntaxError: invalid syntax
>>> a="!@#$%Y"
>>> 'hello priya say masoom to %s and send the code %s'%(b,a)
'hello priya say masoom to hey and send the code !@#$%Y'
>>> a='masoom'
>>> name='masoom'
>>> thing='book'
>>> print("call to {} and give this {} to him"%(name,thing))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print("call to {} and give this {} to him"%(name,thing))
TypeError: not all arguments converted during string formatting
>>> print('call to {} and give this {} to him'formate(name,thing))
SyntaxError: invalid syntax
>>> print("call to {} and give this {} to him"format(name,thing))
SyntaxError: invalid syntax
>>> "call to {} and give this {} to him"format(name,thing)
SyntaxError: invalid syntax
>>> a='masoom'
>>> b='ali'
>>> "{} is the first name and second name is {} format(a,b)
SyntaxError: EOL while scanning string literal
>>> "{} is the first name and second name is {} "format(a,b)
SyntaxError: invalid syntax
>>> "my first name is {} and second name is {}".fromat(a,b)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    "my first name is {} and second name is {}".fromat(a,b)
AttributeError: 'str' object has no attribute 'fromat'
>>> "my first name is {} and second name is {}".format(a,b)
'my first name is masoom and second name is ali'
>>> print("my first name is {} and second name is {}".fromat(a,b))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("my first name is {} and second name is {}".fromat(a,b))
AttributeError: 'str' object has no attribute 'fromat'
>>> print("my first name is {} and second name is {}".format(a,b))
my first name is masoom and second name is ali
>>> 
