def assign_cookies(Student,Cookie) :
    Student.sort()
    Cookie.sort()
    n = len(Student)
    m = len(Cookie)
    satisfied = 0

    i = 0
    j = 0

    while i < n and j < m :
        if Cookie[j] >= Student[i] :
            i += 1
            j += 1
            satisfied += 1
        else :
            j += 1
    return satisfied

print(assign_cookies([1, 2, 2, 3],[1, 2, 2]))