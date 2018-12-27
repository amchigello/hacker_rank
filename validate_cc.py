import re
cc='4424444424442444'
# cc='5124-4567-8912-3456'
pattern1=re.compile('\d{4}-\d{4}-\d{4}-\d{4}$')
pattern1=re.compile('(\d)\1{3}')

valid_flag='Valid'

if (cc.startswith('4') | cc.startswith('5') | cc.startswith('6')) == False:
    valid_flag='Invalid'
    
if ((pattern1.search(cc) is None) & (len(cc)!=16)):
    valid_flag='Invalid'
    
if (cc.isdigit()==False):
    valid_flag='Invalid'
    
if (pattern1.search(cc) is not None):
    valid_flag='Invalid'

    
    
print(valid_flag)    
