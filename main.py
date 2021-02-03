if __name__ == '__main__':
    temperature = input('Δώσε θερμοκρασία: ')
    temperature = int(temperature)

    if temperature <= 0:
        print('Παγετός')
    elif temperature >= 1 and temperature <= 15:
        print('Κρύο')
    elif temperature >= 16 and temperature <= 25:
        print('Φυσιολογική θερμοκρασία')
    elif temperature >= 26 and temperature <= 35:
        print('Ζέστη')
    else:
        print('Καύσωνας')