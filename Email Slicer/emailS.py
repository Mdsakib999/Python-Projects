# Email slicer using python


email_id = input("Enter your Email: ").strip()

user_name = email_id[:email_id.index("@")]

domain_name = email_id[email_id.index("@")+1:]

result = (f"Your name is '{user_name}' and your domain name is '{domain_name}'")

print(result)
