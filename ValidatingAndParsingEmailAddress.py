import email.utils
import re
# print(email.utils.parseaddr('DOSHI <DOSHI@hacker.com')) output: ('DOSHI', 'DOSHI@hackerrank.com')
# print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))) output: DOSHI <DOSHI@hackerrank.com>
email_ids = [email.utils.parseaddr(input()) for _ in range(int(input()))]
for email_id in email_ids:
    if re.match(r"^([a-z]+[a-z0-9-_.]*)@([a-z]+)\.([a-z]{1,3})$",email_id[1]):
        print(email.utils.formataddr(email_id))
