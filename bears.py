def bears(n):
    if n<42:  return False
    if n==42: return True


    b = False
    if n%2 == 0:
        b = bears(n//2)

    give_back = n%10 * ((n//10)%10)
    if (n%3==0 or n%4==0) and b==False and give_back!=0:
        b = bears(n - give_back)

    if n%5==0 and b==False:
        b = bears(n-42)
    
    return b