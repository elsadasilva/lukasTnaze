def fact(n):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    if n<2:
        return 1
    else:
        return n*fact(n-1)

"""
Ajout de la version non récursive
"""

def fact(n):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    x=1
    for i in xrange(2,n+1):
        x*=i
    return x

