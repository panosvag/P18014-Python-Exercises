def maxSequence(l):
    newlist = []
    final_list = []
    max = -1
    for k in range(0,len(l)):            #Για κάθε στοιχείο στην λίστα
        end = 1
        for i in range(0,len(l)):        #Δημιουργεί όλους τουσ δυνατούς δυνδιασμούς λιστών     
            s = 0
            newlist=[]
            for j in range(k,end):
                 s = s + l[j]            #Υπολογίζει το άθροισμα της λίστας
                 newlist.append(l[j])    #Προσθέτει το στοιχείο στο τέλος της λίστας
                 if s > max:             #Αν είναι το μεγαλύτερο άθροισμα
                    max = s              #Αποθηκεύει το άθροισμα
                    final_list = newlist #και την λίστα
            end=end+1 
        
    return max,final_list

l = [-2,1,-3,4,-1,2,1,-5,4]
max,final_list = maxSequence(l)
print(max,':',end=' ')
print(final_list)

    
#ΑΝ ΘΕΛΟΥΜΕ ΝΑ ΕΜΦΑΝΙΖΕΙ ΤΟΥΛΑΧΙΣΤΟΝ 2 ΣΤΟΙΧΕΙΑ ΤΗΣ ΛΙΣΤΑΣ ΠΑΝΤΑ
#(ΓΙΑΤΙ ΥΠΑΡΧΕΙ ΚΑΙ Η ΠΡΙΠΤΩΣΗ ΝΑ ΕΧΩ ΕΝΑΝ ΠΟΛΥ ΜΕΓΑΛΟ ΑΡΙΘΜΟ ΚΑΙ ΟΛΑ ΤΑ ΑΛΛΑ ΑΡΝΗΤΙΚΑ)
#ΤΟΤΕ ΟΙ 5-6 ΓΡΑΜΜΕΣ ΘΑ ΑΛΛΑΧΘΟΥΝ ΣΕ

#  for k in range(0,len(l)-1):
#      end = 2
#      for i in range(0,len(l)-1):
