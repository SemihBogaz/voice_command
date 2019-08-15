Upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
Lower = "abcçdefgğhıijklmnoöprsştuüvyz"


def lower(text: str):
    new_text = str()
    for i in text:
        if i in Upper:
            index = Upper.index(i)
            new_text += Lower[index]
        else:
            new_text += i
    return new_text


