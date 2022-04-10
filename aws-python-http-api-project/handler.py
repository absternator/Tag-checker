import json
import re


def hello(event, context):
    stringToCheck = json.loads(event["body"])["stringToCheck"]
    checkedMessage = checkStringV2(stringToCheck)
    body = {
        "checkedMessage": checkedMessage,
    }
    response = {"statusCode": 200,
                "body": json.dumps(body)}

    return response


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
