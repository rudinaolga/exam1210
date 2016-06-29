import re

def ReadTheText(way):
    text = open(way, encoding = 'utf-8')
    return(text)


def RegEx ():
    m = ReadTheText('examrudina.txt')
    mr = m.read()
    m.close()
    piu = re.findall(r'[А-ЯЁ]+\. [А-ЯЁ]+\. [А-ЯЁ]+[а-яё]\w+', mr)
    piu2 = re.findall(r'[А-ЯЁ]+[а-яё]+ [А-ЯЁ]+[а-яё]\w+', mr)
    for el in piu:
        print(el)
    for a in piu2:
        print(a)
        
def main():
    m = ReadTheText('examrudina.txt')
    RegEx()

if __name__ == '__main__':
    main()
    
