# A basic python program by Abdullah Asim a.k.a Therm1te
# You can use this code to compare between two lists and find the common and mismatched values betweem both
# I have added further comments below through which you can 
# In this case this code will give you all the alphabets there are in names of US States and all which aren't

# Here I am opening the ListNotIn file which contains the list of US States in this case 
# You can add any letters, words etc. to this txt file and use the code with it!

textopen = open('ListNotIn.txt')
textread = textopen.read().splitlines()

# Here I have opened the alphabets both in lower case and upper case 
# I can't lower a list without use of a loop so to make the code short I had to do it)
# You can add any list of words and letters here, not necessary to use with alphabets only
# You can compare two different lists through this!

alphaopen = open('alphabet.txt')
alpharead = alphaopen.read().splitlines()

alphaopenl = open('alphabetl.txt')
alphareadl = alphaopenl.read().splitlines()

# This is the list which will contain all the common elements of the two lists

list_1 = []

# This is the for loop through which Python will cycle through all alphabets and state names
# It will then append that to list_1
# The first loop (below) is for uppercase characters only
# You can uncomment the two print commands below to see the current alphabet and state name being used to check on it.

for l in textread:
    for i in alpharead:
            if i in l:
                # print(i)
                # print(l)
                list_1.append(i)
            else:
                pass

# This command will convert all elements to lowercase including first letters of all strings.

alpharead = [x.lower() for x in alpharead]

# This for loop will cycle through all the lowercase alphabets and state names.
# You can uncomment the two print commands below to see the current alphabet and state name being used to check on it.

for l in textread:
    for i in alpharead:
            if i in l:
                # print(i)
                # print(l)
                list_1.append(i)
            else:
                pass

# Here once again the list is being converted to lower case as I had made two different loops, one for lowercase and one for uppercase.

list_1 = [y.lower() for y in list_1]

# Here Python is converting the list to a dictionary, by doing this all our duplicate values will be removed. 
# The dictionary is being converted back to a list in the same command so there's no need of repeating it.

final_list = list(dict.fromkeys(list_1))

# This will sort the list in a alphabetical order.

final_list.sort

# This is the list of alphabets which are in the name of US States.

print(sorted(final_list), end=" "); print("is in ListNotIn.txt")

#This function will allow us to find the alphabets which aren't in the list of names of US States
# This function is basically converting the list to a set so both elements can be subracted to find out the NotIn characters.

def NotIn(a, b):
    a = set(a)
    b = set(b)
    print(list(b - a), end=" "); print("is not in ListNotIn.txt")

NotIn(final_list, alphareadl)
