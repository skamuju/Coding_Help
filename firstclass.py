


def yell(text):
    return text.capitalize() + "!"

#print(yell('saketh'))

bark = yell

#print(bark)
#print(yell)
#print(bark)

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell()
    else:
        return whisper()

def HELLO(get_speak_func):
    return get_speak_func("Hello", 0.6)
#print(get_speak_func('Hello, World', 0.7)())

functions_l = [bark, get_speak_func]

if __name__ == "__main__":

    #print(yell('hello'))
    #print(functions_l[1]('hello', 0.8))
    print(functions_l[0]('watermelon'))