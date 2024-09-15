import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = re.compile(r"[A-Z][a-zA-Z-']*(?: [A-Z][a-zA-Z-']*)*")
name_regex = re.compile(name)

## NOTE: This is a very simple phone number regex. It will not catch all valid phone numbers. 
##       It is only meant to be used as a starting point for the lab.
phone_number = r"^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
phone_regex = re.compile(phone_number)

## NOTE: This is a very simple email regex. It will not catch all valid email addresses. 
##       It is only meant to be used as a starting point for the lab.
email_address = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)


