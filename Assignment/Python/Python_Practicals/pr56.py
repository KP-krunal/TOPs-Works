# Write a program to check if a list of strings 
# is a valid list of email addresses. 
# eg. ['test@gmail.com','te@rere'] output invalid email list

lst_emails = ['krunal@gmail.com', 'te@rere','netra@gmail.com']

invalid_emails = []

for email in lst_emails:
    if '@' not in email:
        invalid_emails.append(email)
    elif '.' not in email.split('@')[-1]:
        invalid_emails.append(email)
    elif email.count('@') != 1:
        invalid_emails.append(email)


print(invalid_emails)