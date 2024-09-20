ml_of_water = 400 
ml_of_milk = 540
gram_of_coffe_beans = 120
disposable_cups = 9
money = 550
def coffe_machine():
    while True:
        action = input('Write action (buy, fill, take, exit, remaining): ')        
        global ml_of_milk, ml_of_water , gram_of_coffe_beans , disposable_cups, money
        
        if action =='exit':
            break

        elif action == 'remaining':
            print(f'''The coffee machine has:
{ml_of_water} ml of water
{ml_of_milk} ml of milk
{gram_of_coffe_beans} g of coffee beans
{disposable_cups} disposable cups
${money} of money''')
            
        elif action == 'buy':        
            choose_type = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
            if choose_type == 'back':
                pass
            
            elif int(choose_type) == 1:
                if all((ml_of_water >= 250 , gram_of_coffe_beans >= 16)):
                    print('I have enough resources, making you a coffee!')
                    ml_of_water -= 250
                    gram_of_coffe_beans -= 16
                    disposable_cups -= 1
                    money += 4
                
                else:
                    print('Sorry, not enough water!' if ml_of_water < 250 else 'Sorry, not enough coffe beans!')
                    
            elif int(choose_type) == 2:
                
                if all((ml_of_water >= 250 , gram_of_coffe_beans >= 16, ml_of_milk >= 75)):
                    print('I have enough resources, making you a coffee!')
                    ml_of_water -= 350
                    ml_of_milk -= 75
                    gram_of_coffe_beans -= 20
                    money += 7
                    disposable_cups -= 1

                else:
                    if ml_of_milk < 75:
                        print('Sorry, not enough milk!')
                    
                    else:
                        print('Sorry, not enough water!' if ml_of_water < 250 else 'Sorry, not enough coffe beans!' )

            elif int(choose_type) == 3:
                
                if all((ml_of_water >= 250 , gram_of_coffe_beans >= 16, ml_of_milk >= 75)):
                    print('I have enough resources, making you a coffee!')
                    ml_of_water -= 200
                    ml_of_milk -= 100
                    gram_of_coffe_beans -= 12
                    money += 6
                    disposable_cups -= 1
                
                else:
                    if ml_of_milk < 75:
                        print('Sorry, not enough milk!')
                
                    else:
                        print('Sorry, not enough water!' if ml_of_water < 250 else 'Sorry, not enough coffe beans!' )

        elif action == 'fill':
            ml_of_water += int(input('Write how many ml of water you want to add: '))
            ml_of_milk += int(input('Write how many ml of milk you want to add: '))
            gram_of_coffe_beans += int(input('Write how many grams of coffee beans you want to add: '))
            disposable_cups += int(input('Write how many disposable cups you want to add: '))

        elif action == 'take':
            print(f'I gave you ${money}')
            money = 0
coffe_machine()