def ecuacion_recta(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = (y2-y1)/(x2-x1)
    b = y1 + (x1*(y1-y2))/(x2-x1)
    return m, b


a = float(input())
b = float(input())
c = float(input())
d = float(input())
m, b = ecuacion_recta((a,b),(c,d))
print("y="+str(round(m,2))+"x+"+str(round(b,2)))