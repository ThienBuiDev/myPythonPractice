
import re
import pyperclip
#TODO: Create a regex for phone numbers
phoneRegex =  re.compile(r'''
# 123-456-7890, 456-7890, (123) 456-7890, 456-7890 ext. 12345, ext. 12345

(
(\d\d\d|\(\d\d\d\))?#area code(optional)
(\s|-)#first seperator
\d\d\d#first 3 digits 
-#separator
\d\d\d\d#last 4 digits
((ext(\.)? |x)\d{2,5})?
)                  #extension word-part
''',re.VERBOSE)
#TODO: Create a regex for email address

emailRegex = re.compile('[a-zA-Z0-9.%]+@\w+\.\w+')
#TODO: Get the text off the clipboard
text = pyperclip.paste()
#TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
phoneList = []
for i in extractedPhone:
    phoneList.append(i[0])
print(phoneList)
extractedEmail = emailRegex.findall(text)
print(extractedEmail)

#TODO: Copy the extracted email/phone to the clipboard