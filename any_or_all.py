x=[10,14,31,123,121,123]

# res1=[True if val>0 else False for val in x]
# bool1=all([True if val>0 else False for val in x])

# res2=[True if str(val)==str(val)[::-1] else False for val in x]
# bool2=any([True if str(val)==str(val)[::-1] else False for val in x])

# print(bool1 & bool2)

print(all([True if val>0 else False for val in x]) & any([True if str(val)==str(val)[::-1] else False for val in x]))

