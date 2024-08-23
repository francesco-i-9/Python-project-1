import random as rd


def Dadi(cash): 
 
                                            
            puntata = int(input("Quanto vuoi puntare?\n"))
            if puntata > cash:
             print("Saldo insufficiente, riprova")
             return cash
      

            print("Pari o Dispari?")
            p_d = input()
            x=rd.randint(1,6)
            y=rd.randint(1,6)

           

      
          
            if p_d == "Pari" and x+y % 2 == 0:
                        print(x, y)
                        print("Hai vinto!")
                        cash = cash +(puntata*2) 
                        print(cash)
                        return cash
            elif x+y%2 != 0:
                        print(x,y,"\nMi dispiace!")
                        cash = cash-puntata
                        print(cash)
                        return cash
            if p_d == "Dispari" and x+y % 2 !=0:
                        print(x,y)
                        print("Hai vinto")
                        cash = cash+(puntata*2)
                        print(cash)
                        return cash
            elif x+y % 2 == 0:
                        print(x,y,"\nMi dispiace")
                        cash = cash - puntata
                        print(cash)
                        return cash

def Menu(cash):
         risposta = input("Benvenuto!\n-Gioca\n-Controlla\n")
         if risposta.lower() == "gioca":
              scelta_gioco=input("-Dadi\n")
              if scelta_gioco == "Dadi":
                  if cash>0:
                      while cash > 0:
                              cash = Dadi(cash)
                              
                              
                              risp1=(input("Continuare(si/no)?"))
                              if cash == 0 and risp1 == "si":
                                       print("Saldo insufficiente, ricarica\n-Tornare al menù?")
                                       risp2=input()
                                       if risp2.lower() == "si":
                                               Menu(cash)
                              
                                       
                                               

                              if risp1 == "no":
                                     Menu(cash)
                  else: 
                         print("Saldo insufficiente non puoi giocare\n-Tornare al menù?")
                         risp_=input()
                         if risp_.lower()== "si":
                                Menu(cash)
                        
                         
                                    

                              




         if risposta.lower() == "controlla":
                 
                 while True:
                  print("Saldo disponibile:",cash)
                  risp3 =input("Vuoi fare altro?\n")
                  
                  if risp3 == "no":
                   Menu(cash)
                         
                         
                                      
                                      
              

cash = int(input("Quanti soldi hai\n"))
if cash >= 5000:
        Menu(cash)
                
       
           


