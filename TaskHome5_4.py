def encode(sequence):
    count = 1
    result = []

    for x,item in enumerate(sequence): 
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
            if count == 9:
                result.append((sequence[x - 1], count))
                count = 0
        else:        
            result.append((sequence[x - 1], count))
            count = 1            
    
    result.append((sequence[len(sequence) - 1], count))

    return result


def decode(text):
    result = []
    item = 0
    while item < len(text):
        if (text[item].isdigit()):
            result.append(int(text[item]) * (text[item + 1]))
            item += 2
        else: 
            result.append(text[item])
            item += 1
    return "".join(result)


def formatOutput(sequence):
    
    result = []

    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])

    return "".join(result)


with open('file5_4_1.txt', 'r', encoding = 'utf-8') as data:
    txt = data.read()

encoded = encode(txt)

with open('file5_4_2.txt', 'w', encoding = 'utf-8') as data:
    data.write(formatOutput(encoded))

with open('file5_4_3.txt', 'r', encoding = 'utf-8') as data:
    txt2 = data.read()

decoded = decode(txt2)

with open('file5_4_4.txt', 'w', encoding = 'utf-8') as data:
    data.write(decoded)