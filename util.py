def split_lst(lst, delim_func = lambda x:True):
    res = [[]]

    for elem in lst:
        if delim_func(elem):
            res.append([])
        else:
            res[-1].append(elem)

    return res

def lcs(X, Y, key = lambda x:x):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
    R = [[None]*(n + 1) for i in range(m + 1)]
    S = [[None]*(n + 1) for i in range(m + 1)]
    E = [[None]*(n + 1) for i in range(m + 1)]
    """
    Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]
    """

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
                R[i][j] = [[], []]
            elif key(X[i-1]) == key(Y[j-1]):
                L[i][j] = L[i-1][j-1] + 1

                elif L[i][j] == L[i-1][j]:
                    R[i][j] = R[i-1][j]
                elif L[i][j] == L[i][j-1]:
                    R[i][j] = R[i][j-1]
                else:
                    R[i][j] = [R[i-1][j-1][0] + [X[i-1]], R[i-1][j-1][1] + [Y[j-1]]]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

                if L[i-1][j] >= L[i][j-1]:
                    R[i][j] = R[i-1][j]
                else:
                    R[i][j] = R[i][j-1]

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    # return L[m][n]
    return R[m][n]