print("*****      Val Studios Online Ticket System       *****")
ticketa = input("Please Enter Your Name (Only First Name)... \n")
ticketb = input("Please Enter Your Adhaar ID Number... \n")
ticketc = input("Please Enter Your Age... \n")
ticketd = (ticketb)[:4]
identi = (ticketa + "42231" + ticketc + ticketd)
moviedb = int(input("Please Select Your Movie For Flixing \n 1.Brahmastra \n 2.Rajaverta \n 3.Tiger Zinda Hai \n 4.Raabta \n"))
if moviedb == 1:
    max1 = print("Movie ID : Brahmastra \n " + "User ID : " + identi + "\n Price : 480Rs /- Seat")
elif moviedb == 2:
    max2 = print("Movie ID : Rajaverta \n " + "User ID : " + identi + "\n Price : 230Rs /- Seat")
elif moviedb == 3:
    max3 = print("Movie ID : Tiger Zinda Hai \n " + "User ID : " + identi + "\n Price : 130Rs /- Seat")
elif moviedb == 4:
    max4 = print("Movie ID : Raabta \n " + "User ID : " + identi + "\n Price : 290Rs /- Seat")
else :
    print("Sorry You Have Selected A Invalid Character.. !")

Pay = int(input("Please Enter The Above Amount To Confirm Your Ticket \n"))
print("Seat Confirmed")
Seats = int(input("How Many Seat Would You Like To Aquire...\n"))
total = (Seats * Pay )
tax = float(4.56/100*(total))
print("Moving Towards Final Gateway.....")
print("Billing...\n")
print("Your Grand Total Bill Is " + str(total) + "RS According to your Selectives")
print("---------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------")
print("Your Grand Total Including Tax Amount is = " + str(total + tax) + "Rs /-" )
print("---------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------")
