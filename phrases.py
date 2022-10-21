from random import choice
import bot

def read_phrases():
    global content_list
    with open("./resources/phrases.txt") as f:
        content_list = f.readlines()
    content_list = [x.strip() for x in content_list]
    
def get_phrase():
    selector = choice(content_list)
    return selector