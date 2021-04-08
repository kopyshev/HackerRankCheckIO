def checkio(text, word):
    text=text.lower()
    l = len(word)
    first_letter= word[0]    
    text_list = [[c for c in l.replace(" ", "")] for l in text.split("\n")]
    rows = len(text_list)
    for i in range(rows):
        for j in range(len(text_list[i])):
            if text_list[i][j] == first_letter:
                if len(text_list[i])-j >=l and "".join(text_list[i][j:j+l])==word: 
                    return [i+1,j+1,i+1,j+l]
                if rows-i >=l and "".join([row[j] if len(row)>j else "#" for row in text_list][i:i+l])==word: 
                    return [i+1,j+1,i+l,j+1]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    assert checkio("""Hi all!
And all goodbye!
Of course goodbye.
or not""", "haoo") == [1, 1, 4, 1]
    assert checkio("""xa
xb
x""", "ab") == [1, 2, 2, 2]
print("Coding complete? Click 'Check' to earn cool rewards!")