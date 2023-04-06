# * if number of argument is known
def kids(*kids):
    print('youngest child is ' + kids[1])


kids('Joy', 'Fany', 'Jule')

print('-----------------')
#  ** number of argument aren't known


def freinds(**freind):
    print('My best freind is ' + freind['cyb'])


freinds(prog='python', cyb='metasploit')


print('------------------------ \n\n')
# pass a list as argument


def m_tools(tool):
    print("I'm currenty experiment: \n")
    for i in tool:
        print('- ' + i)


m_tools(['nmap', 'ngrock', 'wireshark', 'socialIr'])
