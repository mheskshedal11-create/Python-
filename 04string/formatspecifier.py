'''
 Format specifires= {value:flags} format a value based on what flags are inserted

 
 Format	     Meaning	                      Example
 :d	         Integer	                      {age:d} → 25
 :f	         Float	                          {pi:f} → 3.141590
 :.2f	     Float 2 decimals	              {pi:.2f} → 3.14
 :s	         String	                          {name:s} → Alice
 :<10	     Left-align 10 spaces	          {name:<10} → 'Alice '
 :>10	     Right-align 10 spaces	          {name:>10} → ' Alice'
 :^10	     Center-align 10 spaces	          {name:^10} → ' Alice '
 :03d	     Pad integer with zeros	          {num:03d} → 007
 :,	         Thousand separator	              {money:,.2f} → 1,234,567.89

'''

price1= 3.14159
price2=-987.1555
price3= 12.34


print(f'price 1 is:  {price1:>10}')
print(f'price 2 is:  {price2:^10}')
print(f'price 3 is:  {price3:<10}')
