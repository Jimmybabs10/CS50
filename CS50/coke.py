accepted_denomination = [25, 10, 5]
change = 50

while change > 0:
    # print(change)
    # change -= 10
    amount_paid = int(input('please insert coin:      '))
    if amount_paid in accepted_denomination:
        change = (change - amount_paid)
        if change <= 0:
            amount_owed = change * -1
            print(f'amount owed: {amount_owed}')
        else:
            print(f'amount due: {change}')
    elif amount_paid not in accepted_denomination:
        print(f'amount due: {change}')
    else:
        continue
