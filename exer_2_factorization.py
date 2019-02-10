def is_prime(n):
#Δέχεται έναν φυσικό αριθμό μεγαλύτερο της μονάδας και επιστρέφει True αν είναι πρώτος αλλιώς επιστρέφει False
    d = 0                          #το πλήθος των διαιρετών του αριθμού
    for i in range(1,n+1):
        if n%i == 0:
            d+=1
    if d == 2:                     #αν το πλήθος των διαιρετών είναι 2 τότε διαιρείται μόνο από τον ευατό του και την μονάδα
        return True
    else:
        return False

def factorization(n):
    factor_list=[]
    i=2
    while n != 1 :
        if is_prime(i):
            while n%i == 0:
                factor_list.append(i)
                n//=i
        i+=1
    return factor_list


while True:
    
    try:
        x = int(input('Δώσε έναν ακέραιο θετικό αριθμό μικρότερο ή ίσο του 1000000:'))
        if (x >=1 and x <= 1000000):
            break
    except:
        print('Δεν πληκτρολογήσατε αριθμό')
    

f = factorization(x)
s = set(f)               #Δημιουργώ ένα σύνολο για να πάρω μία φορά τους παράγοντες
f_unique = list(s)       #Αντιγράφω το σύνολο σε μια νέα λίστα γιατί τα σύνολα δεν ταξινομούνται
f_unique.sort()          #Ταξινομώ την νέα λίστα

#Εμφανίζω την ανάλυση πρώτων παραγόντων 

for item in f_unique:
    x = f.count(item)
    if x == 1:
        print('(',item,')',end='')
    else:
        print('(',item,'**',x,')',end='')




