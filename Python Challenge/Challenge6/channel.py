import re, zipfile

number_list = []
comment_list = []



with zipfile.ZipFile("channel.zip") as zipper:
    with zipper.open("channel/29.txt") as file:
        print(file.read().decode("utf-8"))
        info = zipper.getinfo('channel/29.txt')
        print(info.comment)

##
##def NextFile(num):
##    num = num[0]
##    file = open("channel/" + str(num) + ".txt")
##    file = file.read()
##    number = re.findall('([0-9].*$)', file)
##    return number
##
##
##file = open("channel/29.txt")
##
##list_comments = []
##
##list_comments.append(file.comment)
##
##print(list_comments)
##file = file.read()
##number = re.findall('([0-9].*$)', file)
##for i in range(0,1000):
##    print(number)
##    number = NextFile(number)
