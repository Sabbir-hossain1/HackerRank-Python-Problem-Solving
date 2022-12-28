# Instructions*

# *Put / at start and at end if you want to use it in real world( programming language)

# Rule

# Must be Valid
# Regular Expressions for URLs

# ^(?:http|https|ftp):\/\/[a-zA-Z0-9_~:\-\/?#[\]@!$&'()*+,;=`^.%]+\.[a-zA-Z0-9_~:\-\/?#[\]@!$&'()*+,;=`^.%]+$
# -----------------------------------------------------------------------
# Valid URLs

# http://foo.com/blah_blah
# http://foo.com/blah_blah?
# http://fooTV.us
# http://foo.com/blah_blah_(wikipedia)
# https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains
# http://foo.com/blah_blah_(wikipedia)_(again)
# http://www.example.com/wpstyle/?p=364
# https://www.example.com/foo/?bar=baz&inga=42&quux
# http://df.ws/123
# http://userid:password@example.com:8080
# http://userid:password@example.com:8080/
# http://userid@example.com
# http://userid@example.com/
# http://userid@example.com:8080
# http://userid@example.com:8080/
# http://userid:password@example.com
# http://userid:password@example.com/
# http://142.42.1.1/
# http://142.42.1.1:8080/

# Link to see domains

# https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

import re
re.match(r"^(?:http|https|ftp):\/\/[a-zA-Z0-9_~:\-\/?#[\]@!$&'()*+,;=`^.%]+\.[a-zA-Z0-9_~:\-\/?#[\]@!$&'()*+,;=`^.%]+$","http://sabbir.com")