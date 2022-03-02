hello = "hello"
world = "world"

def add_words_together(word_a, word_b):
    result = word_a + " " + word_b
    return result

hello_world = add_words_together(hello, world)
goodbye_world = add_words_together("goodbye", "world")

print(hello_world)
print(goodbye_world)