import unittest

def transpose(m):
    return [ [ m[c][r] for c in range(0, len(m)) ] for r in range(0, len(m[0])) ]

def matmul(m1, m2):
    retval = []
    for r in range(0, len(m1)):
        retval.append([])
        for c in range(0, len(m2[0])):
            sum = 0
            for i in range(0, len(m1[r])):
                sum = sum + m1[r][i]*m2[i][c]
            retval[r].append(sum)
    return retval


def exchange_rows(m, i, j):
    (i, j) = (i, j) if i < j else (j, i)
    return m[0:i] + [m[j]] + m[i+1:j] + [m[i]] + m[j+1:]

def add_multiple(m, r1, r2, factor):
    retval = m.copy()
    for c in range(0, len(m[0])):
        retval[r1][c] += m[r2][c]*factor
    return retval

def multiply_by(m, r, factor):
    retval = m.copy()
    for c in range(0, len(m[0])):
        retval[r][c] *= factor
    return retval

    
def gaussian_elimination(m):
    for r in range(0, len(m)):
        for c in range(1,2):
            None




            



class Test(unittest.TestCase):
    def test_transpose(self):
        m = [[1,2,3],[4,5,6]]
        mT = [[1,4],[2,5],[3,6]]
        self.assertEqual(transpose(m), mT)
        self.assertEqual(transpose(mT), m)

    def test_matmul(self):
        m1 = [[1,2]]
        m2 = [[3],[4]]
        self.assertEqual(matmul(m1, m2), [[11]])

    def test_exchange_rows(self):
        m = [[1,1],[1,2],[3,4],[5,6]]
        self.assertEqual(exchange_rows(m, 2, 3), [[1,1],[1,2],[5,6],[3,4]])

    def test_add_multiple(self):
        m = [[1,1],[1,2],[3,4],[5,6]]
        self.assertEqual(add_multiple(m, 1, 3, 2), [[1,1],[11,14],[3,4],[5,6]])

    def test_multiply_by(self):
        m = [[1,1],[1,2],[3,4],[5,6]]
        self.assertEqual(multiply_by(m, 1, 3), [[1,1],[3,6],[3,4],[5,6]])

unittest.main()