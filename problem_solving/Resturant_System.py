# Resturant SYSTEM 
class Resturant:  
        
        def options(self):
            print(".......WELCOME TO THE RESTURANT...........\n\n")
            print("For DESI MENU Press 1")
            print("For CONTINENTAL MENU Press 2")
            print("FOR CHINESE MENU PRESS ")    

                  
        def menu(self,optionx):
                if optionx ==1:
                    Desi_menu={
                        "Chicken Karhai":35,
                        "Chicken Kabab":45,
                        "Chicken Mughlai":56,
                        "Raishmi Kabab":100,
                        "Chicken Bryani":400,
                        "Chicken Pulao":350,
                        "Beef Pulao":200,
                        "Beef Rosh":300
                    }
                    for key,values in Desi_menu.items():
                        print(f"Dish Name:{key} -> Price:RS {values}")

                elif optionx ==2:
                                Continental_menu={
                                    "Pasta":100,
                                    "Kung pao Chicken":120,
                                    "Chicken Shashlik":150,
                                    "Chicken Chowmien":90,
                                    "Pad Thai":450,
                                    "Prawns with Rice":350,
                                    "Smoked Salmon ":500,
                                    "Sushies 6 pcs ":1000
                                }
                                for key,values in Continental_menu.items():
                                    print(f"Dish Name:{key} -> Price:RS {values}")
                
                elif optionx ==3:
                                Chinese_menu={
                                    "EGG NOODLES":25,
                                    "Egg Fried Rice":45,
                                    "Beef Noodles":56,
                                    "TOFU SOUP":300
                                    }
                                for key,values in Chinese_menu.items():
                                    print(f"Dish Name:{key} -> Price:RS {values}")

class Order(Resturant):
       def place_order(self):
              return 
              
              


       


R1=Resturant()
attempt=0
while True:
        R1.options()
        try:
            x=int(input("ENTER THE OPTION :"))   
            if x in [1,2,3]:              
                R1.menu(x)
                break
            else:
                    attempt+=1
                    print("Please Enter the Invalid Option ")

                    if attempt==3:
                           print("You are unauthorised now Please Restart the program")
                           break

        except ValueError:
               attempt+=1
               print("Please Enter the Number Only ")
               if attempt==3:
                  print("You are unauthorised now Please Restart the program")
                  break
            
