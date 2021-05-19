name = input('What is your name?: ')
#print('Hi', name, 'How can i help you?: ')

def main():

	calc=input(f'Hi {name}, what do you want to calculate: ')
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

	elif calc == 'wavelength':
		frequency=int(input('Frequency: '))
		print('Wave length: ', 3*10**8/frequency, 'm/s')
		solution=input('Do you want to see the steps?(yes or no): ')
		if solution == 'yes':
			print('Wavelength= speed of light/frequency')
			print('=3*10**8/frequency')    
			print(f'=3*10**8/{frequency}')
			print('Wavelength: ', 3*10**8/frequency,'Hz')
		if solution == 'no':
			print('Ok')

	elif calc == 'energy of a photon when planks constant and frequency are given':
		frequency=int(input('Frequency: '))
		Energy_of_a_photon=6.63*10**-34 * frequency
		print('Energy of Photon: ', 6.63*10**-34 * frequency)
		ev=input('Are you converting into electron volts? (yes or no): ')
		if ev == 'yes':
			print('converting to electron volts...')
			print('converting to electron volts...')
			print('converting to electron volts...')
			print('converting to electron volts...')
			
			print('Energy of a photon(ev) : ', 1.602*10**-19*Energy_of_a_photon, 'j')
		elif ev == 'no':
			print('ok')
		solution=input('Do you want to see the steps?(yes or no): ')
		if solution == 'yes':
			print('Energy of Photon: ', 'planks constant * frequency')
			print('Energy of Photon: ', '6.63*10**-34 * frequency')
			print(f'Energy of Photon:  6.63*10**-34 * {frequency}')
			print('Energy of photon: ', 6.63*10**-34 * frequency,'J')
		if solution == 'no':
			print('Ok')

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
		solution=input('Do you want to see the steps?(yes or no): ')
		if solution == 'yes':
			print('Energy of Photon: ', 'planks constant * speed of light / wave length')
			print('Energy of Photon: ', '6.63*10**-34 * 3*10**8 / wave length')
			print(f'Energy of Photon:  6.63*10**-34 * 3*10**8 / {Wavelength}')
			print('Energy of photon: ', 6.63*10**-34 * 3*10**8 / Wavelength,'J')
		if solution == 'no':
			print('Ok')

	elif calc == 'work function':
		threshold_frequency=int(input('Threshold Frequency: '))
		print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')
		solution=input('Do you want to see the steps?(yes or no): ')
		if solution == 'yes':
			print('Work function: planks constant * threshold frequency')
			print('6.63*10**-34 * threshold frequency')
			print(f'6.63*10**-34 * {threshold_frequency}')
			print('Work function: ', 6.63*10**-34*threshold_frequency, 'j')
		
	elif calc == 'energy of a photon when work function and kinetic energy are present':
		kinetic_energy_work_function = input('Were kinetic energy given and work function?: ')
		if kinetic_energy_work_function == 'yes':
			KE = int(input('Kinetic Energy: '))
			work_function2 = int(input('Work function: '))
			result = print('Energy of photon: ', work_function2 + KE, 'j')
			print(result)
		if kinetic_energy_work_function == 'no':
			mass = int(input('Mass: '))
			velocity = int(input('Velocity: '))
			KE2 = (0.5 * mass * velocity)
			threshold_frequency3 = int(input('Threshold frequency: '))
			work_function3 = (6.63*10**-34 * threshold_frequency3)
			print('Energy of a photon: ', KE2 + work_function3, 'j')
	
	elif calc == 'what can you calculate':
		print('I can calculate:\n frequency\n wavelength\n energy of a photon when planks constant and frequency are given\n energy of a photon when planks constant, speed of light, and wavelength are given\n energy of a photon in electron volts\n percentages\n quadratic equations\n work function')

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

	elif calc == 'addition':
		num1 = int(input('First number: '))
		num2 = int(input('Second number: '))
		add = num1 + num2
		print(add)

	elif calc == 'subtraction':
		num1 = int(input('First number: '))
		num2 = int(input('Second number: '))
		sub = num1 - num2
		print(sub)

	elif calc == 'multiplication':
		num1 = int(input('First number: '))
		num2 = int(input('Second number: '))
		mul = num1 * num2
		print(mul)

	elif calc == 'division':
		num1 = int(input('First number: '))
		num2 = int(input('Second number: '))
		div = num1 / num2
		print(div) 

	else:
		print('I do not understand')

	Repeat = input('Do you want to perform another operation?(yes or no): ').lower()
	if Repeat == 'yes': 
		main()

	else:
		print('Bye', name)
		exit()
main()




