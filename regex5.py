"""

For Example:

w{3,5} : It will match the character w ,  or  times.
[xyz]{5,} : It will match the character x, y or z  or more times.
\d{1, 4} : It will match any digits , , , or  times.

Task

You have a test string .
Your task is to write a regex that will match  using the following conditions:

 should begin with  or  digits.
After that,  should have  or more letters (both lowercase and uppercase).
Then  should end with up to  . symbol(s). You can end with  to  . symbol(s), inclusively.
Note

This is a regex only challenge. You are not required to write any code.
You have to fill the regex pattern in the blank (_________).
"""

Regex_Pattern = r'^[0-9]{1,2}[A-Za-z]{3,}(\.){0,3}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())