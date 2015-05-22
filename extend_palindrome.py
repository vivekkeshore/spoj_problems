while True:
    try:
        text = raw_input().strip()
    except EOFError:
        break

    text_len = len(text)
    i = text_len/2
    flag = False
    while i > 0:
        if text[i-1] == text[text_len - i]:
            i -= 1
        else:
            flag = True
            break

    if flag:
        index = 0
        while flag:
            ext_text = text + text[index::-1]
            ext_len = len(ext_text)
            i = ext_len/2
            while i > 0:
                if ext_text[i-1] == ext_text[ext_len - i]:
                    i -= 1
                else:
                    flag = False
                    break

            if flag:
                text = ext_text
                break
            else:
                index += 1
                flag = True

    print text

    # text_len = len(text)
    # i = text_len/2
    # flag = True
    # while i > 0:
    #     if text[i-1] == text[text_len - i]:
    #         i -= 1
    #     else:
    #         flag = False
    #         break
    #
    # if not flag:
    #     index = text.find(text[text_len-1])
    #     if text_len-1 == index:
    #         index = text_len - 1
    #     z = 0
    #     while z+index < (index+text_len)/2:
    #         if text[index + z] == text[text_len - z - 1]:
    #             z += 1
    #             continue
    #         else:
    #             index += z
    #
    #     text += text[index-1::-1]
    #
    # print text
