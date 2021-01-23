# function for encrypting to a1z26 cause i'm lazy
def A1Z26_encrypt(cistring):
    string = []
    cistring = cistring.lower()
    cistring = "".join(cistring.split())
    for x in range(0, len(cistring)):
        char = ord(cistring[x]) - 96
        if char > 0 and char <= 26: string.append(int(char)-1)
    return(string)

# define variables
o=["Avocados", "Bandanas", "Carrots", "Drums", "Elephants", "Flashlights", "Grapes", "Highlighters", "Incentives", "Jacks", "Kangaroos", "Lemons", "Muffins", "Ninjas", "Olives", "Pears", "Quizzes", "Raisins", "Submarines", "Turnips", "Umbrellas", "Violas", "Watermelons", "X-Rays", "Yards", "Zebras"]
a=["Acidic", "Broke", "Confused", "Determined", "Exothermic", "Fragrant", "Green", "Hilarious", "Insincere", "Juicy", "Keen", "Lovely", "Misty", "New", "Orange", "Purple", "Quick", "Red", "Stoic", "Troubling", "Underwhelmed", "Victorious", "Warm", "Xeric", "Young", "Zesty"]
s=["Always", "Bravely", "Calmly", "Daringly", "Easily", "Fondly", "Gladly", "Honestly", "Instantly", "Joyfully", "Kindly", "Loudly", "Magically", "Neatly", "Openly", "Perfectly", "Quietly", "Rarely", "Safely", "Tenderly", "Usually", "Victoriously", "Warmly", "Xerically", "Yearly", "Zestfully"]
c=["Award", "Bother", "Conduct", "Drive", "Evaluate", "Form", "Give", "Help", "Inspect", "Jump", "Keep", "Lift", "Memorize", "Notice", "Officiate", "Pursue", "Quiz", "Raise", "Switch", "Turn", "Underwhelm", "Vacate", "Wish", "X-Ray", "Yield", "Zip"]

# the actual start of the code
print("what is your peardeck code?: ")
i = input().lower()
ilist = A1Z26_encrypt(i)
try:
	temp = a[ilist[0]]
except IndexError:
	print("ERROR: Please input letters.")
except:
	print("ERROR: Unknown error occurred!")
if (len(i) == 6):
	print(a[ilist[0]] + " ", end="")
	print(o[ilist[1]] + " ", end="")
	print(s[ilist[2]] + " ", end="")
	print(c[ilist[3]] + " ", end="")
	print(a[ilist[4]] + " ", end="")
	print(o[ilist[5]], end="")
elif (len(i) == 5):
	print(a[ilist[0]] + " ", end="")
	print(o[ilist[1]] + " ", end="")
	print(c[ilist[2]] + " ", end="")
	print(a[ilist[3]] + " ", end="")
	print(o[ilist[4]], end="")
else:
	print("invalid input, exiting")
	exit()
