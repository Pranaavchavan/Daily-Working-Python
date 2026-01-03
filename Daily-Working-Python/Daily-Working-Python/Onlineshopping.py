print("Welcome to patil Online shopping Store")
print("""
    1.Electronics
    2.Grocerries
    3.Clothing
    4.exit    """)
choice=int(input("Enter your choice"))
if choice==1:
    print("""
          1.Mobile  (25000)
          2.Tv      (40000)
          3.laptop  (30000)
          4.exit""")
    choice1=int(input("enter your choice"))
    if choice1==1:
        price=25000
        print("you have selected mobile")
    elif choice1==2:
        price=40000
        print("you have selected Tv")
    elif choice1==3:
        price=30000
        print("you hace slected laptop")
    elif choice1==4:
        print("thanks for shopping electronics")
    else:
        print("invalid choice")
elif choice==2:
    print("""
          1.Sakhar  30/kg
          2.Nirma   40/kg
          3.Oil     100/kg
          4.exit
          """)
    choice2=int(input("Enter your choice"))
    if choice2==1:
        price=30
        print("you have slected for sakhar")
    elif choice2==2:
        price=40
        print("you have slected nirma")
    elif choice2==3:
        price=100
        print("Oil is selected")
    elif choice2==4:
        print("thankd= you for visiting")
    else:
        ("invalid choice")
elif choice==3:
    print("""
          1.Shirt Rs.500
          2.Pants RS.800
          3.Tshirt Rs.300
          4.exit
          """)
    choice3=int(input("enter your choice"))
    if choice3==1:
        price=500
        print("you have slected for Shirt")
    elif choice3==2:
        price=800
        print("you have slected Pant")
    elif choice3==3:
        price=300
        print("TSHIRT is selected")
    elif choice3==4:
        print("thank you for visiting")
    else:
        ("invalid choice")
elif choice==4:
    print("Exit")
    print("thanks for visiting")
    
else:
    print("invalid choice")

quantity=int(input("Enter quantity"))
discount=0
total=price*quantity

if total>30000:
    discount=total*0.20
    print("you got 20% discount")
elif total>15000:
    discount=total*0.10
    print("you got 10 % discount")
else:
   print("no discount")

finalAmount=total-discount
print("you got discount rs",discount)
print("final amount is rs",finalAmount)
           