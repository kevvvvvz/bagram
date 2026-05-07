print("Player 2 is Computer.")

def turnOrder():
    while True:
        first = input("Do you want to start the game? (Yes/No): ").capitalize()
        if first == "Yes":
            chance = input("Enter 'F' for first chance. Enter 'S' for second chance: ")
            if chance == 'F':
                return 'F'
            elif chance == 'S':
                return 'S'
        elif first == "No":
            print("Game Over!")
            return None
        else:
            print("Please enter only Yes or No")
        
def turn(myList):
    
    updated = myList
    
    while True:
        try:
            if updated and updated[-1] == 20:
                print("You must enter 21!")
                amount = 1
            else:
                amount = int(input("How many numbers do you wish to enter? "))
            if 1 <= amount <= 3:
                currentNum = []
                i = 0
                if updated:
                    last = updated[-1]
                else:
                    last = 0
                    
                while i < amount:
                    numbers = int(input("Enter your numbers one at a time: "))
                    expected = last + 1
                    if numbers != expected:
                        print(f"Error: You must enter {expected}")
                        continue
                    elif numbers == expected:
                        last = numbers
                        currentNum.append(numbers)
                        i += 1
                break
            else:
                print("You can enter at most 3 numbers. Please select an amount 1-3.")
        except ValueError:
            print("Please enter a valid number.")
        #print(currentNum)
    combined = updated + currentNum
    return combined



def compTurn(myList):
    current = myList
    newList = []
    multiples = [4, 8, 12, 16, 20]
    
    if not current:
        last = 0
        print("Order of inputs after computer's turn is:")
        newList.append(1)
        combined = []
        combined = current + newList
        print(combined)
        return combined
    else:
        last = current[-1]
    
    nextMultiple = None
    for num in multiples:
        if num > last:
            nextMultiple = num - last
            break
    
    if nextMultiple is None:
        nextMultiple = 1
        
    if nextMultiple > 3:
        nextMultiple = 3
    
    print("Order of inputs after computer's turn is:")
    for i in range(1, nextMultiple + 1):
        newList.append(last + i)
    #print(newList)
        
    combined = []
    combined = current + newList
    print(combined)
    return combined
    


def main():
    choice = turnOrder()
    if choice is None:
        return
    numbers = []
    
    # Computer goes first
    if choice == 'S':
        numbers = compTurn(numbers)
        while True:
            # Your Turn
            numbers = turn(numbers)
            if numbers[-1] >= 21:
                print("Computer wins!")
                break
            
            # Computer Turn
            numbers = compTurn(numbers)
            if numbers[-1] >= 21:
                print("Player wins!")
                break
        
    if choice == 'F':
        while True:
            # Your Turn
            numbers = turn(numbers)
            if numbers[-1] >= 21:
                print("Computer wins!")
                break
            
            # Computer Turn
            numbers = compTurn(numbers)
            if numbers[-1] >= 21:
                print("Player wins!")
                break
        
main()