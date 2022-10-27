import re
word_dict = {}
word_list = []
filename = input("Please input the filename you want to test:")#input the filename you want to test
reserveWord = ["auto", "break", "case", "char", "const",
            "continue", "default", "do", "double", "else",
            "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return",
            "short", "signed", "sizeof", "static", "struct",
            "switch", "typedef", "union", "unsigned",
            "void", "volatile", "while", "elseif"]#reserveWord in C++
def get_file():#get the file we want to get
    f = open(filename,'r',encoding='UTF-8')
    file = f.read()
    #Only leave the content we want to leave
    symbol_list = ["+", "-", "*", "/", "<", "<=", ">", ">=", "=", "==",
     "!=", ";", "(", ")", "^", ",", "\"", "\'", "#", "&",
     "&&", "|", "||", "%", "~", "<<", ">>", "[", "]", "{",
     "}", "\\", ".", ":", "!"]  #the symbols in C++
    for i in symbol_list:
        file = file.replace(i," ")#replace unwanted symbols
    f.close()
    return file
def get_words():#split the words in order for us to test
    file = get_file().replace('else if','elseif')
    separator = [r'//.*', r'\/\*(?:[^\*]|\*+[^\/\*])*\*+\/', r'".*"']
    for i in separator:
        word_list = re.split(i,file)
        new_file = ""
        for word in word_list:
            new_file+=word
    word_list = new_file.split()
    return word_list
words = get_words()
def first_level():
    count = 0
    words = get_words()
    for i in words:
        if i in reserveWord:
            word_dict[i] = word_dict.get(i,0)+1
            word_list.append(i)
            count+=1
    count = count+word_dict.get("elseif",0)
    return count+1
def second_level():
    new_list = []
    count1 = 0
    count2 = 0
    count_list = []
    for i in get_words():
        if i=='switch' or i == 'case':
            new_list.append(i)
    for i in new_list:
        if i=='switch':
            count1 += 1
        return count1
    length = len(new_list)
    print("case num:",end='')
    for i in range(0,length-1):
        if ((new_list[i]=='switch') and (new_list[i+1]=='case')) or ((new_list[i]=='case') and (new_list[i+1]=='case')):
            count2=count2+1
        if new_list[i]=='case' and new_list[i+1]=='switch' or i==length-2:
            count_list.append(count2)
            count2=0

    return count_list
def third_level():
    print()
    if_list= []
    count = 0
    for i in words:
        if i=='if' or i=='else' or i=='elseif':
            if_list.append(i)
    length = len(if_list)
    for i in range(length-1):
        if if_list[i]=='if' and if_list[i+1]=='else':
            count+=1
    return count
def fourth_level():
    test_list=[]
    count = 0
    for i in words:
        if i =='if':
            test_list.append(i)
        elif i == 'elseif' and test_list[-1]!='elseif':
            test_list.append(i)
        elif i == 'else':
            if test_list[-1] == 'elseif':
                test_list.pop()
                test_list.pop()
                count += 1
    return count
level = int(input("Please input the level you want to test:"))
def dispaly():
    if level == 1:
        first_level()
    elif level == 2:
        first_level()
        second_level()
    elif level == 3:
        first_level()
        second_level()
        third_level()
    elif level == 4:
        first_level()
        second_level()
        third_level()
        fourth_level()
    else:
        print("Please input valid number!")
dispaly()