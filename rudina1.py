import re

def ReadTheText(way):
    text = open(way, encoding = 'utf-8')
    return(text)


def RegEx ():
    m = ReadTheText('examrudina.txt')
    mr = m.read()
    m.close()
    res = re.findall('[А-ЯЁ]\. [А-ЯЁ][а-яё]+\w', mr)
    if res != None:
        for el in res:
            print(el)

def main():
    m = ReadTheText('examrudina.txt')
    RegEx()

if __name__ == '__main__':
    main()
    
