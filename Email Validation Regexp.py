# Instructions*

# *Put / at start and at end if you want to use it in real world( programming language)

# Rules

# Include a-zA-Z
# Must have   @
# Numbers,  symbols allowed
# Valid
# No Consecutive double dots are allowed


# Valid emails as per wikipedia.org

# x@example.com
# prettyandsimple@example.com
# very.common@example.com
# disposable.style.email.with+symbol@example.com
# other.email-with-dash@example.com
# fully-qualified-domain@example.com
# example@s.solutions
# best%@best.com
# #!$%&'*+-/=?^_`{}|~@example.org
# admin@regex101.com.au

# Invalid emails as per wikipedia.org

# admin@regex101.com.au.
# 1234567890123456789012345678901234567890123456789012345678901234+x@example.com
# john..doe@example.com
# john.doe@example..com
# A@b@c@example.com

import re
re.match(r"^(?!.*\.\.)[\w.\-#!$%&'*+\/=?^_`{}|~]{1,35}@[\w.\-]+\.[a-zA-Z]{2,15}$","example@gmail.com")