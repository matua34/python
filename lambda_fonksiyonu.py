#atamasız syılarda topplam

a = input("first number put:")
b = input("second number put:")
c = input("third number put:")
#kullanıcıdan sayılar girmesinin istedik
def _sum(a,b,c):
    return((a+c)/100*b)
_sum(int(a),int(b),int(c))

#lambda fonksiyonu
new_sum = lambda a,b,c: ((a+c)/100*b)
new_sum(int(a),int(b),int(c))

sıra = [("a",5),("c",3),("b",9),("e",6)]
sorted(sıra, key = lambda x: x[1])








