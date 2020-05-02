# 🔑 Password checker 
---

A simple python script that uses a [have I been pwned password api](https://haveibeenpwned.com/API/v3) to check if a password has been leaked.

## How to use it:

The script will check for the passwords on the files that you pass to it via command line
```py
 python checkmypass password_file1.txt password_file2.txt ... password_filen.txt
```
and will output how many times a specific password has been found on the leaked password database.
```
The password qwerty was found 3912816 on the leaked password database! You should not use this password!
The password dghfahddfgaydf2342342378462374fdfar57675 was NOT found on leaked password database. You can use that!
The password moon was found 16009 on the leaked password database! You should not use this password!
```
