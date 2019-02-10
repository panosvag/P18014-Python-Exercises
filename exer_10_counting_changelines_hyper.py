import codecs
while True:
    try:
        fl=input('Δώστε το όνομα του html αρχείου: ')
        f = codecs.open(fl, 'r','utf-8') 
        break
    except FileNotFoundError as exc1:
        print(exc1)
        
lines = f.readlines()
cl = 0          #πλήθος αλλαγών γραμμής από <br>
clp = 0         #πλήθος αλλαγών γραμμής από <p>.Υπολογίζεται επί 2 αφού έχω μια αλλαγή γραμμήσ πριν και μία μετά
hyper = 0       #πλήθος υπερσυνδέσμων
for line in lines:
    changelines = line.count('<br>')
    paragraphs = line.count('</p>')
    hyperlinks = line.count('<a href=')
    cl += changelines
    clp += paragraphs
    hyper += hyperlinks
clp *=2
print('Πλήθος υπερσυνδέσμων :',hyper)
print('Πλήθος αλλαγής γραμμής από παράγραφο <p>:',clp)
print('Πλήθος αλλαγής γραμμής από <br>:',cl)
print('Συνολικό Πλήθος αλλαγής γραμμής από <br> και <p>:',cl+clp)

f.close()

