# 12 Hour Format

# Hour
# (0?[1-9]|1[012])
# Minutes
# [0-5]?[0-9]
# Seconds
# [0-5]?[0-9]
# Complete

# ^(?:0?[1-9]|1[012]):(?:[0-5]?[0-9])(?::[0-5]?[0-9])?(?: am| pm| AM| PM)?$
# -------------------------------
# 24 Hour Format

# Hour
# (0?[0-9]|1[0-9]|2[0-3])
# Minutes
# [0-5]?[0-9]
# Seconds
# [0-5]?[0-9]

# Complete

re.match(r"^(?:0?[0-9]|1[0-9]|2[0-3]):(?:[0-5]?[0-9])(?::[0-5]?[0-9])?(?: GMT| EST)?$") 