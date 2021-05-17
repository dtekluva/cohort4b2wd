another_calc = True

while another_calc != "no":

    print('Welcome to my calculator')

    calc=input('What do you want to calculate: ')  
    print('You have selected: ', calc)

    if calc == 'frequency':
        Wavelength=int(input('Wave Length: '))
        print('Frequency: ', 3*10**8/Wavelength,'Hz') 
        solution=input('Do you want to see the steps?(yes or no): ')
        if solution == 'yes':
            print('Frequency = speed of light/wavelength')
            print('=3*10**8/Wavelength')    
            print(f'=3*10**8/{Wavelength}')
            print('Frequency: ', 3*10**8/Wavelength,'Hz')
        if solution == 'no':
            print('Ok')

    #################################
    ######   OLD POSITION    ########
    #################################

    # another_calc = input('Do you want to perform another operation?(yes or no): ')
    # if another_calc == 'yes': 
    #     #i want to make refrence to the first calc and if caloc
    #     calc = input('What do you want to calculate: ')
    #     print('You have selected: ', calc)
    # if another_calc == 'no':
    #     print('ok')

    #################################
    ######   OLD POSITION    ########
    #################################


    elif calc == 'wavelength':
        frequency=int(input('Frequency: '))
        print('Wave length: ', 3*10**8/frequency, 'm/s')

    elif calc == 'energy of a photon when planks constant and frequency are given':
        frequency=int(input('Frequency: '))
        Energy_of_a_photon=6.63*10**-34/frequency
        print('Energy of Photon: ', 6.63*10**-34/frequency)
        ev=input('Are you converting into electron volts? (yes or no): ')
        if ev == 'yes':
            print('converting to electron volts...')
            print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon, 'j')
        elif ev == 'no':
            print('ok')

    elif calc == 'energy of a photon when planks constant, speed of light, and wavelength are given':
        Wavelength=int(input('Wave length: '))
        Energy_of_a_photon2=6.63*10**-34*3*10**8/Wavelength
        print('Energy of photon: ',6.63*10**-34*3*10**8/Wavelength, 'j')
        ev=input('Are you converting into electron volts? (yes or no): ')
        if ev == 'yes':
            print('converting to electron volts...')
            print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon2, 'j')
        elif ev == 'no':
            print('ok')

    elif calc == 'work function':
        threshold_frequency=int(input('Threshold Frequency: '))
        print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')

    elif calc == 'what can you calculate':
        print('I can calculate:\n frequency\n wavelength\n energy of a photon when planks constant and frequency are given\n energy of a photon when planks constant, speed of light, and wavelength are given\n I can also calculate energy of a photon in electron volts')

    elif calc == 'what can you calculate under energy of a photon':
        print('I can calculate quite a number of things. I can calculate: energy of a photon when planks constant and frequency are given,\n energy of a photon when planks constant, speed of light, and wavelength are given')

    elif calc == 'quadratic equation':
        a=int(input('a: '))
        b=int(input('b: '))
        c=int(input('c: '))
        d = (b**2 - 4*a*c)**2/2*a
        e = -b + d, -b - d 
        print(f'x is equal to: {e}')

    elif calc == 'percentage':
        num=int(input('Enter given number: '))
        num2=int(input('Enter the percentage given: '))
        print(num2/100*num)


    #################################
    ######   NEW POSITION    ########
    #################################

    another_calc = input('Do you want to perform another operation?(yes or no): ')
    if another_calc == 'yes': 
        #i want to make refrence to the first calc and if caloc
        calc = input('What do you want to calculate: ')
        print('You have selected: ', calc)
    if another_calc == 'no':
        print('ok')

    #################################
    ######   NEW POSITION    ########
    #################################