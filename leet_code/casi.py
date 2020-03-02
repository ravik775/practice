import numpy as np

def getLetter(n):
    if n < 13:
        return 'A'
    elif n < 27:
        return 'B'
    return 'C'

n = 0
cn_a, cn_b, cn_c = 0, 0, 0
r_cn = {1: 0, 2: 0, 3:0}
Lookup = dict( (i, (1, getLetter(i), 'E' if i%2 == 0 else 'O'))  for i in range(1, 37, 3))
Lookup.update((i, (2, getLetter(i), 'E' if i%2 == 0 else 'O'))  for i in range(2, 37, 3))
Lookup.update((i, (3, getLetter(i), 'E' if i%2 == 0 else 'O'))  for i in range(3, 37, 3))

history = []
nums = [[i, 1] for i in range(37)]

while 0 <= n:
    if 0 <= n < 37:
        nums[n][1] += 1
        if n != 0 :
            row, c, EvenOdd = Lookup[n] 
            if c == 'A':
                cn_a += 1
            elif c == 'B':
                cn_b += 1
            else:
                cn_c += 1
            r_cn[row] += 1
            history.append('{0}{1} {2} {3}'.format(c,row, EvenOdd, 'L' if n <=18 else 'R'))
            
            m_a = min(x[1] for x in nums if  0 <  x[0] < 13 ) 
            m_b = min(x[1] for x in nums if 13 <= x[0] < 27 )
            m_c = min(x[1] for x in nums if 27 <= x[0]  )
            
            c_a = [n[0] for n in sorted((x for x in nums if 0 < x[0] < 13 and x[1] <= m_a), key=lambda x:x[1])]
            c_b = [n[0] for n in sorted((x for x in nums if 13 <= x[0] < 27 and x[1] <= m_b), key=lambda x:x[1])]
            c_c = [n[0] for n in sorted((x for x in nums if 27 <= x[0] and x[1] <= m_c), key=lambda x:x[1]) ]
           
            for en in history[-10:]:
                print (en)
            
            rc = r_cn[1]+ r_cn[2]+ r_cn[3]
            cc = (cn_a + cn_b + cn_c) 
            
            row_p = (0, r_cn[1]/rc, r_cn[2]/rc , r_cn[3]/rc ) 
            col_p = (cn_a/cc, cn_b/cc, cn_c/cc)
            
            
            print("{0:.2f}  {1:.2f} {2:.2f}".format(row_p[3]* col_p[0], row_p[3]*col_p[1], row_p[3]*col_p[2]))
            print("{0:.2f}  {1:.2f} {2:.2f}".format(row_p[2]* col_p[0], row_p[2]*col_p[1], row_p[2]*col_p[2]))
            print("{0:.2f}  {1:.2f} {2:.2f}".format(row_p[1]* col_p[0], row_p[1]*col_p[1], row_p[1]*col_p[2]))
            print("%s %s %s "%  (c_a, c_b, c_c ))
    try:
        n = int(input("Enter number:").strip() or 0)
    except:
        n = 0
 
print ("%s" % history)