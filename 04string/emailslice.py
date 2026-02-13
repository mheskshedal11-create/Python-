email =input('Enter you email: ')

index = email.index('@')

username=email[:index]

domain= email[index+1:]
print(index)
print(f'username is: {username}')
print(f'domain name is: {domain}')