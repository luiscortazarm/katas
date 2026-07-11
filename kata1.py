class Dictionary:
    def __init__(self):
        # Initialize an empty dictionary to store words and definitions
        self.entries = {}

    def newentry(self, word, definition):
        # Add a new word-definition pair example
        self.entries[word] = definition

    def look(self, word):
        # Look up the definition or return a default message
        return self.entries.get(word, f"Can't find entry for {word}")

# Example Usage:
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
d.newentry('Potatoe', 'A vegetable that grows in the ground')
print(d.look('Apple'))   # A fruit that grows on trees
print(d.look('Banana'))  # Can't find entry for Banana
print(d.look('Potato'))  #A vegetable that grows in the ground
