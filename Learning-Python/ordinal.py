#getting ordinal number of characters
#neumerical value of ASCII character 

print(ord('H'))

print(ord('\n'))


#every string in python in any language in is string(only unicode in python2)
x = '안녕하세요'
print(type (x))

y = u'세요'
print(type (y))

#regular string and unicode string are the same in python 3 
#regular string and byte(raw) sting are different in python 3
#decode() uses ASCII or UFT-8 since compatible --> turns bytes to unicode
#encode() uses ASCII or UFT-8 since compatible --> turns string to bytes