from dice import Dice,Die

def main():
    n=int(input("Enter the number of dice to roll: "))
    dice=Dice()

    for i in range(n):
        die=Die()
        dice.addDie(die)

    while True:
        dice.rollAll()
        print("YOUR ROLL: ",end=" ")
        for die in dice.list:
            print(die.value,end=" ")
        print("\n")

        choice=input("Wanna roll again? (y/n): ")
        if choice!="y":
            print("Bye!")
            break

if __name__=="__main__":
    main()

        
