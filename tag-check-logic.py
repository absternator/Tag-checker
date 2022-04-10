import re


def checkString(s: str) -> str:
    length = len(s)
    st = []
    for i in range(length):
        if(s[i] == '<' and i + 2 < length and re.match('<[A-Z]>', val := s[i:i+3])):
            st.append(val)

        elif(s[i] == '<' and i + 3 < length and re.match('</[A-Z]>', val := s[i:i+4])):
            if(st):
                if st[-1][1] == val[2]:
                    st.pop()
                else:
                    return (f"expected </{st[-1][1]}> found {val}")
            else:
                return (f"Expected # found {val}")
    if st:
        return (f"expected </{st[-1][1]}> found #")
    return ('Correctly tagged paragraph')


def checkStringV2(stringToCheck: str) -> str:
    length = len(stringToCheck)
    openingTagStack = []
    i = 0
    while(i < length):
        if(stringToCheck[i] == '<' and i + 2 < length and re.match('<[A-Z]>', openingTag := stringToCheck[i:i+3])):
            openingTagStack.append(openingTag)
            i += 3
        elif(stringToCheck[i] == '<' and i + 3 < length and re.match('</[A-Z]>', closingTag := stringToCheck[i:i+4])):
            if(openingTagStack):
                if openingTagStack[-1][1] == closingTag[2]:
                    openingTagStack.pop()
                    i += 4
                else:
                    return (f"Expected </{openingTagStack[-1][1]}> found {closingTag}")
            else:
                return (f"Expected # found {closingTag}")
        else:
            i += 1

    if openingTagStack:
        return (f"Expected </{openingTagStack[-1][1]}> found #")
    return ('Correctly tagged paragraph')


s = ' <B> </B>'
a = 'The following text<C><B>is centred and in boldface</B></C>'
b = '<B>This <\g>is <B>boldface</B> in <<*> a</B> <\6> <<d>sentence'
c = '<B><C> This should be centred and in boldface, but the tags are wrongly nested</B></C>'
d = '<B>This should be in boldface, but there is an extra closing tag</B></C>'
e = '<B><C>This should be centred and in boldface, but there is a missing closing tag</C>'
print(checkStringV2(e))
