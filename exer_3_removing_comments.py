while True:
    try:
        fl=input('Δώστε το όνομα του αρχείου που θα γίνει απαλειφή σχολίων: ')
        f = open(fl, 'r') 
        break
    except FileNotFoundError as exc1:
        print(exc1)
        
lines = f.readlines()
fnew=open('file2.txt', 'w') 
for line in lines:
    if not line.strip():   # Διατηρεί τις κενές γραμμές   
        fnew.writelines(line)
    else:        #Ελέγχει ότι υπάρχει στην γραμμή # Αν δεν υπάρχει την γράφει στο νέο αρχείο
        com_sign_pos = line.find('#')    
        if (com_sign_pos<0):    
            fnew.writelines(line)
        else:                                       #Υπάρχει χαρακτήρας #
            if line.startswith('#'):                #Αν ξεκινάει με # δεν την γράφει καθόλου
                continue
            else:
                quote_pos= line.find("'")           #Ελέγχει αν υπάρχει χαρακτήρας '
                if (quote_pos<0):                   # Αν δεν υπάρχει υπάρχει σχόλιο στο τέλος της γραμμής και το αφαιρεί
                    line = line.split('#')
                    stripped_string = line[0].rstrip()
                    fnew.writelines(stripped_string)
                    fnew.writelines('\n')
                else:                               #Υπάρχει και ' και #
                    quote_left_pos = line.index("'")                    #Βρίσκει την θέση του αριστερού '
                    quote_right_pos = line.rindex("'")                  #Βρίσκει τη θέση του δεξιού '
                    com_sign_right_pos = line.rindex('#')               #Βρίσκει τη θέση του δεξιού #
                    if (com_sign_right_pos > quote_right_pos):          #Αν η τελευταία θέση του # είναι μεγαλύτερη από την τελευταία θέση ενός ΄ τότε υπάρχει σχόλιο στα δεξιά και το αφαιρεί
                        start = line[:com_sign_right_pos]
                        end = line[com_sign_right_pos:]
                        fnew.writelines(start)
                        fnew.writelines('\n')
                    else:                           #αλλιώς ο χαρακτήρας # είναι μέσα σε '' και τον αγνοεί
                        fnew.writelines(line)
                        
fnew.close()

#INPUT FILE
#line1
#line2
#line3 'str in quotes without comment'
#comment at the begging
#line4 #comment at the end
#line5 'str in quotes with #' something   #comment at the end
#line6 'str in quotes with # and no comments at the end' something
#line7


#OUTPUT FILE
#line1
#line2
#line3 'str in quotes without comment'
#line4
#line5 'str in quotes with #' something   
#line6 'str in quotes with # and no comments at the end' something
#line7













