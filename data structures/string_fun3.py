from data import story

words = story.split()
print(f"total characters in the story: {len(story)} ")
print(f'total number of word = {len(words)}')
print(f'total unique words in the story = {len(set(words))}')
print(words)

sentences = story.split('.')
print(f'total number of sentences = {len(sentences)}')

lines = story.split('\n')
print(f'total lines in the story = {len(lines)}')

poem_list = [
    'Twinkle, Twinkle, little star,',
    'How I wonder what you are!',
    'Up above so world so high,',
    'Like a dimond in the sky.'
    ]

poem = "\n".join(poem_list)
print(poem)
