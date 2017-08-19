alpha = list('abcdefghijklmnopqrstuvwxyz')

def scramble(text):
    text=text.lower()
    for i in range(len(alpha)):
        if i < (len(alpha)-1):
            text = text.replace(alpha[i],alpha[i+1].upper())
        else:
            text = text.replace(alpha[i],alpha[0].upper())
    text = text.replace(' ', '#')
    text = text.replace(':', '?')
    text = text.replace('1', '!')
    text = text.replace('2', '@')
    text = text.replace('3', '{')
    text = text.replace('4', '$')
    text = text.replace('5', '%')
    text = text.replace('6', '^')
    text = text.replace('7', '&')
    text = text.replace('8', '*')
    text = text.replace('9', '-')
    text = text.replace('0', ':')
    return text[::-1]

def unscramble(text):
    text = text[::-1]
    text = text.replace(':', '0')
    text = text.replace('-', '9')
    text = text.replace('*', '8')
    text = text.replace('&', '7')
    text = text.replace('^', '6')
    text = text.replace('%', '5')
    text = text.replace('$', '4')
    text = text.replace('{', '3')
    text = text.replace('@', '2')
    text = text.replace('!', '1')
    text = text.replace('?', ':')
    text = text.replace('#', ' ')
    for i in range(len(alpha)):
        if i > 0:
            text = text.replace(alpha[i].upper(),alpha[i-1])
        else:
            text = text.replace(alpha[i].upper(),alpha[25])
    return text
