import string


def fun(s):
    parts = s.split('@')
    if len(parts) != 2:
        return False
    else:
        if (username(parts[0])) and (len(parts[0]) != 0):
            extension = parts[1].split('.')
            if (len(extension) == 2) and (len(extension[1]) < 4):
                if website(extension[0]) and website(extension[0]):
                    return True
        else:
            return False


def username(name):
    return set(name) <= allowed


def website(name):
    return set(name) <= allowed_site

#def fun(s):
#    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
#    return(a)

lst = []
allowed = set(string.ascii_letters + string.digits + '_' + '-')
allowed_site = set(string.ascii_letters + string.digits)
i = input()
for j in range(int(i)):
    line = input()
    if fun(line):
        lst.append(line)
lst.sort()
print(lst)