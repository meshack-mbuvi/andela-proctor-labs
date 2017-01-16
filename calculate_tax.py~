def calculate_tax(kwargs):
    if type(kwargs) == type({}):
        def tax_bill(amount, total_tax = 0):
            if amount < 1000:
                total_tax = 0
                
            else:
                total_tax += 0
                remainder = amount - 1000
                  
                if remainder >= 9000:
                    total_tax += (9000 * 0.1)
                    remainder -= 9000
                    
                    if remainder >= 10200:
                        total_tax += (10200 * 0.15)
                        remainder -= 10200
                        
                        if remainder >= 10550:
                            total_tax += (10550 * 0.2)
                            remainder -= 10550
                            
                            
                            if remainder >= 19250:
                                total_tax += (19250 * 0.25)
                                remainder -= 19250
                                
                                if remainder >= 50000:
                                    total_tax += (remainder * 0.3)
                                else:
                                    total_tax += (remainder * 0.3)                         
                            else:
                                total_tax += (remainder * 0.25)
                                                        
                        else:
                            total_tax += (remainder * 0.2)                
                    else:
                        total_tax += (remainder * 0.15)
                else:
                    total_tax += (remainder*0.1)
                    
            return total_tax
        
        return_tax_bill = {}
        for k, v in kwargs.items():
            if type(v) == type(''):
                raise ValueError('Allow only numeric input')
            else:
                return_tax_bill[k] = tax_bill(v)
            
        return return_tax_bill
    else:
        raise TypeError("The provided input is not a dictionary.")
        
        
    
tax = {'Alex': 500,'James': 20500, 'Kinuthia': 70000}
m = {}
not_dict = [234, 456]
#print(calculate_tax(not_dict))
print(calculate_tax(tax))
print(calculate_tax({'mesh':600}))
