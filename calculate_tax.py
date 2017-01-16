def calculate_tax(kwargs):
  if type(kwargs)==type({}):
    d={}
    for key,val in kwargs.items():
      if type(val)==type(''):
        raise ValueError('Allow only numeric input')
      #initialize tax varible
      tax=0
      if val>1000:
        if val>10000:
          tax+=(10000-1000)*0.1
        else:
          tax+=(val-1000)*0.1

      #tax for values above 10000
      if val>10000:
        if val>20200:
          tax+=(20200-10000)*0.15
        else:
          tax+=(val-10000)*0.15
      #tax for values above 20200
      if val>20200:
        if val>30750:
          tax+=(30750-20200)*0.2
        else:
          tax+=(val-20200)*0.2
      #tax for values above 30750
      if val>30750:
        if val>50000:
          tax+=(50000-30750)*0.25
        else:
          tax+=(val-30750)*0.25
      #tax for values above 50000
      if val>50000:
        tax+=(val-50000)*0.3
      d[key]=tax
    return d
  else:
    raise ValueError ('The provided input is not a dictionary.')
        
        
    
tax = {'Alex': 500,'James': 20500, 'Kinuthia': 70000}
m = {}
not_dict = [234, 456]
#print(calculate_tax(not_dict))
print(calculate_tax(tax))
print(calculate_tax({'mesh':600}))
