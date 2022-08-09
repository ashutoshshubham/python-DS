from data import story

print(f"total characters in the story: {len(story)} ")

#count substring in large string

a_count = story.count('a')
print(f'a occurs {a_count} times')
the_count = story.lower().count("the")
print(f'the occurs {the_count} times')

#replace 
ustory = story.replace('of','on')
print(ustory)

#removing data
ustory = story.replace('a','')
print(ustory)

#removing all vowels
no_vowel_story = story.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print(no_vowel_story)

#retaining all vowels
only_vowel_story = ''
for char in story:
    if char in 'aeiouAEIOU':
        only_vowel_story = only_vowel_story +char
print(only_vowel_story)

