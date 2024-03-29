"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

"""
def minion_game(string):
    sturt_count = 0
    kevin_count = 0
    length = len(string)

    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin_count += (length-i)
        else:
            sturt_count += (length - i )
    if sturt_count > kevin_count:
        print("Stuart"+" "+str(sturt_count))
    elif kevin_count > sturt_count:
        print("Kevin"+" "+str(kevin_count))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)