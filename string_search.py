# What if I did not have search in strings functionality in Python and had to write one

def findInString(str, pattern):
    if len(pattern) > len(str):
        return -1
    elif len(str) == 0 or len(pattern) == 0
        return -1

    s_arr = [c for c in str]
    p_arr = [c for c in pattern]
    startIndex = -1

    for index, cs in enumerate(s_arr):
        i = 0

        for iIndex, cp in enumerate(p_arr):
            if cs == cp and i == 0:
                i += 1
                startIndex = index
            elif i > 0 and index + i + 1 <= len(s_arr) and cp == s_arr[index + i]:
                i += 1

                if iIndex + 1 == len(p_arr):
                    break
            else:
                i = 0
                startIndex = -1
                break

        if startIndex > -1:
            break

    return startIndex


print(findInString("Hello world, are you still spinning?", "world"))
print(findInString("Hello world, are you still spinning?", "still"))
print(findInString("Hello world, are you still spinning?", "are"))
print(findInString("Hello world, are you still spinning?", "john"))
print(findInString("Hello world, are you still spinning?", "Hello world, are you still spinning??"))
