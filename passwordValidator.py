#! python3

import re, pyperclip

passwordRegex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

password = str(pyperclip.paste())

mo = passwordRegex.findall(password)

if not mo:

    print('Password is not strong. Please, consider changing it.')

else:

    print('Password is strong.')