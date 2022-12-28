# Instructions*
# *Put / at start and at end if you want to use it in real world( programming language)

# Rulues
# Include a-zA-Z
# Must start with A-Z
# No Numbers 
# No Symbols
# . , and space are allowed
# Length
# No Consecutive double spaces,commas,dot are allowed
import re
re.match(r"^(?!.*\s\s)(?!.*\.\.)(?!.*,,)[A-Z][a-zA-Z.,]{2,30}$")