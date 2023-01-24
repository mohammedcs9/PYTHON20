# Regular Expresssions => Re Module Search And FindAll
# search()/findall()
import re

#my_search = re.search("[A-Z]", "OsamaElzero")
my_search = re.search(r"[A-Z]{2}", "OOsamaElzero")

print(my_search)
#print(dir(my_search))
print(my_search.span())
print(my_search.string)
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:

    print("this is a valid email")

    print(is_email.span())
    print(is_email.string)
    print(is_email.group())

else:

    print("this is a valid email")

email_input = input("please write your email: ") 

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

    empty_list.append(search)

    print("email added")

else:

    print("invalid email")

for email in empty_list:

    print(email)        