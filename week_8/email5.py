'''
.          any character except a newline
*          0 or more repetitions
+          1 or more repetitons
?          0 or 1 repetitions
{m}        m repetitions
{m,n}      m-n repetitions

'''
import re

email = input("Email: ").strip()

if re.search(".+@.+",email):
    print("Valid")
else:
    print('Invalid')