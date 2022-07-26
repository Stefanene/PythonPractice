with open('tarzan.txt') as f:
    intext = f.read()

outtext = ""

lines = intext.split('\n')
for line in lines:
    words = line.split(' ')
    for word in words:
        afterstr = ""
        if word.__contains__('<'):
            afterstr = word[word.index('>')+1:]   # get suffix
            word = input(f"Please input a {word[1:word.index('>')]}> ")  # ask for replacement word
        outtext += f" {word}{afterstr}"  # add to end result

print(f"  =={outtext}")

