#Eleni Maria Fili
print('Welcome to #PARTA_OLA game')
players=eval(input('please give the number of players:'))
lst=[]
for i in range(1,players+1):
    lst.append(i)
if players >= 2:
    b=eval(input('Please give the number of beans per player:'))
    print('-----------------------------------------------')
    ROUND=1
    print('Round',ROUND,'begins!Every player has to put a bean!')
    b=b-1
    first_time=1
    Pot=players
    lst1=[]
    for m in range(1,players+1):
            lst1.append(b)
    e=['Put one','Put two','Take one','Take two','Take them all','All players put one']
    while Pot>0 and lst1.count('none')<len(lst1)-1 :
        import random
        ra=random.randint(0, len(e)-1)
        p=e[ra]
        print('Current state:');print('Pot:',Pot)
        for j in range(0,len(lst)):
            if lst[j]!='none':
                print( 'Player',lst[j],'has',lst1[j],'beans')
        print(

                           )
        while first_time==1:
            r=random.randint(1, len(lst))
            print('Player',r,'is your turn!',p)
            first_time = first_time+1
            break
        else :
               if r <= len(lst):
                     while lst[r-1]=='none':
                         if r==len(lst):
                             r=1 
                         for i in range (r,len(lst)):
                             r+=1
                             break
                     else:
                         print('Player',r,'is your turn!',p)
                         if r==len(lst):
                             r=1
               else:
                    r=1
                    while lst[r-1]=='none':
                       for i in range (r,len(lst)):
                           r+=1
                           break
                    else:
                        print('Player',r,'is your turn!',p)  
        if p==e[0] :
            if lst1[r-1]=='none':
                r=r
            elif lst1[r-1] <= 0:
                print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                del lst1[r-1],lst[r-1]
                lst.insert(r-1,'none')
                lst1.insert(r-1,'none')
            else:
                Pot+=1
                lst1[r-1]-=1
        elif p==e[1]:
            for o in range(1,3):
                if lst1[r-1]=='none':
                    r=r
                elif lst1[r-1] <= 0 :
                    print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                    del lst1[r-1],lst[r-1]
                    lst.insert(r-1,'none')
                    lst1.insert(r-1,'none')
                else:
                    Pot+=1
                    lst1[r-1]-=1
        elif p==e[2]:
            if Pot==0:
                r=r
            elif lst1[r-1]=='none':
                r=r
            elif lst1[r-1] < 0:
                print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                del lst1[r-1],lst[r-1]
                lst.insert(r-1,'none')
                lst1.insert(r-1,'none')
            else:
                Pot-=1
                lst1[r-1]+=1
        elif p==e[3]:
            for o in range(1,3):
                if Pot==0:
                    r=r
                elif lst1[r-1]=='none':
                        r=r
                elif lst1[r-1] < 0:
                    print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                    del lst1[r-1],lst[r-1]
                    lst.insert(r-1,'none')
                    lst1.insert(r-1,'none')
                else:
                    Pot-=1
                    lst1[r-1]+=1
        elif p==e[4]:
            if Pot==0:
                r=r
            elif lst1[r-1]=='none':
                r=r
            elif lst1[r-1] < 0:
                print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                del lst1[r-1],lst[r-1]
                lst.insert(r-1,'none')
                lst1.insert(r-1,'none')
            else:
                lst1[r-1]=lst1[r-1]+Pot
                Pot-=Pot    
        else:
            if lst1.count(0)==len(lst1):
                    print("That's a draw!")
                    Pot=-1
            for d in range(1,len(lst)+1):
                if lst1[d-1]=='none':
                    d=d
                elif lst1[d-1] <= 0:
                    print('Player',d,'has',lst1[d-1],'beans.You \'re out.')
                    del lst1[d-1],lst[d-1]
                    lst.insert(d-1,'none')
                    lst1.insert(d-1,'none')
                else:
                    Pot += 1
                    lst1[d-1]-=1
                    if lst1[d-1]<0:
                         print('Player',d,'has',lst1[d-1],'beans.You \'re out.')
                         del lst1[d-1],lst[d-1]
                         lst.insert(d-1,'none')
                         lst1.insert(d-1,'none')         
        r+=1
        if lst.count('none')==len(lst)-1 :
            Pot=0         
    else:
        ROUND+=1
        for m in range(0,len(lst)):
            if lst1[m]==0 :
                print('Player',lst[m],'has',lst1[m],"beans.You 're out!")
                del lst1[m],lst[m]
                lst.insert(m,'none')
                lst1.insert(m,'none')
        #gt mporei ston 1o gyro na exoun bgei oloi ektos 1os kai to pot na einai 0...
        while lst1.count('none')<len(lst1)-1 and Pot>=0:
            import random
            ra=random.randint(0, len(e)-1)
            p=e[ra]
            if Pot==0:
                print('Pot:',Pot,'...Round ends')
                for j in range(0,len(lst)):
                    if lst[j]!= 'none':
                        print( 'Player',lst[j],'has',lst1[j],'beans')
                print('-----------------------------------------------');print('Round',ROUND,'begins!Every player has to put a bean!')
                ROUND+=1
                for m in range(0,len(lst)):
                    if lst1[m]=='none' or lst1[m]==0 :
                        if lst1[m]==0:
                            print('Player',lst[m],'has',lst1[m],"beans.You 're out!")
                        del lst1[m],lst[m]
                        lst.insert(m,'none')
                        lst1.insert(m,'none')
                    else:
                        lst1[m]-=1
                        Pot+=1
                        
            print('Current state:')
            print('Pot:',Pot)
            for j in range(0,len(lst)):
                if lst[j]!='none':
                    print( 'Player',lst[j],'has',lst1[j],'beans')
            print(
                                )                                             
            
            if r <= len(lst):
                while lst[r-1]=='none':
                         if r==len(lst):
                             r=1 
                         for i in range (r,len(lst)):
                             r+=1
                             break
                else:
                         print('Player',r,'is your turn!',p)
                         if r==len(lst):
                             r=1
            else:
                r=1
                while lst[r-1]=='none':
                    for i in range(r,len(lst)):
                        r+=1
                        break
                else:
                    print('Player',r,'is your turn!',p) 

            if p==e[0] :
                if lst1[r-1]=='none':
                    r=r
                elif lst1[r-1] <= 0:
                    print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                    del lst1[r-1],lst[r-1]
                    lst.insert(r-1,'none')
                    lst1.insert(r-1,'none')
                else:
                    Pot+=1
                    lst1[r-1]-=1
            elif p==e[1]:
                for o in range(1,3):
                    if lst1[r-1]=='none':
                        r=r
                    elif lst1[r-1] <= 0 :
                        print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                        del lst1[r-1],lst[r-1]
                        lst.insert(r-1,'none')
                        lst1.insert(r-1,'none')
                    else:
                        Pot+=1
                        lst1[r-1]-=1
            elif p==e[2]:
                if Pot==0:
                    r=r
                elif lst1[r-1]=='none':
                    r=r
                elif lst1[r-1] < 0:
                    print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                    del lst1[r-1],lst[r-1]
                    lst.insert(r-1,'none')
                    lst1.insert(r-1,'none')
                else:
                    Pot-=1
                    lst1[r-1]+=1
            elif p==e[3]:
                for o in range(1,3):
                    if Pot==0:
                        r=r
                    elif lst1[r-1]=='none':
                        r=r
                    elif lst1[r-1] < 0:
                        print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                        del lst1[r-1],lst[r-1]
                        lst.insert(r-1,'none')
                        lst1.insert(r-1,'none')
                    else:
                        Pot-=1
                        lst1[r-1]+=1
            elif p==e[4]:
                if Pot==0:
                    r=r
                elif lst1[r-1]=='none':
                    r=r
                elif lst1[r-1] < 0:
                    print('Player',r,'has',lst1[r-1],'beans.You \'re out.')
                    del lst1[r-1],lst[r-1]
                    lst.insert(r-1,'none')
                    lst1.insert(r-1,'none')
                else:
                    lst1[r-1]=lst1[r-1]+Pot
                    Pot-=Pot    
            else:
                if lst1.count(0)==len(lst1):
                    print("That's a draw!")
                    Pot=-1
                for d in range(1,len(lst)+1):
                   if lst1[d-1]=='none':
                       d=d
                   elif lst1[d-1] <= 0:
                        print('Player',d,'has',lst1[d-1],'beans.You \'re out.')
                        del lst1[d-1],lst[d-1]
                        lst.insert(d-1,'none')
                        lst1.insert(d-1,'none')
                   else:
                        Pot += 1
                        lst1[d-1]-=1
                        if lst1[d-1]<0:
                             print('Player',d,'has',lst1[d-1],'beans.You \'re out.')
                             del lst1[d-1],lst[d-1]
                             lst.insert(d-1,'none')
                             lst1.insert(d-1,'none')  
            r+=1
        else:
            for j in range(0,len(lst)):
                if lst1[j]!='none':
                    print('Player',lst[j],'CONGRATULATIONS!!!YOU ARE THE WINNER!!!')
else:
    print('Attention: 2+ players')

