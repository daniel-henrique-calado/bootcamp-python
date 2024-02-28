"""
Remove duplicate e-mail on the following list
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
"""

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
unique_emails = set(emails)
print(unique_emails)