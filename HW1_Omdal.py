#Name: Megan Omdal
#Date: 09-08-2022
#Description: This program prompts the user to enter a dollar amount to be converted,
#             calculates the conversion into Euro, Yuan, Peso, and Yen currencies and
#             prints the dollar amount and the conversion.
#====================================================================================================================================================
#
#Declarations:
Dollars = 1.00
Euro = 0.00
Yuan = 0.00
Peso = 0.00
Yen = 0.00

#Input:
Dollars = eval(input("Enter the dollar amount: "))  #prompts the user to enter the dollar amount
#Calculations:
Euros = Dollars * 0.97 #converts Dollars to Euros
Yuan = Dollars * 6.93  #converts Dollars to Yuan
Peso = Dollars * 19.97  #converts Dollars to Peso
Yen = Dollars * 140.37  #converts Dollars to Yen

#Output:
print("You have entered " , Dollars, "dollars." , "\nConverted to... " , "\nEuro(European Union): ", round(Euros, 2),
      "\nYuan(China):" , round(Yuan, 2) , "\nPeso(Mexico): " , round(Peso, 2) , "\nYen(Japan): " , round(Yen, 2))   #displays the converted currencies 

#========================================================================================================================================================
