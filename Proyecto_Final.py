import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print(' ')
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  rounds += 1

  if not user_option in options:
    print("Ingresa una opción válida")
    continue

  computer_option = random.choice(options)

  print('Opción del user => ', user_option)
  print('Opción de la compu => ', computer_option)

  if user_option == computer_option:
    print('EMPATEEEEEEEE')

  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('GANA EL USER!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('GANA LA COMPUU')
      computer_wins += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('GANA EL USER!')
      user_wins += 1
    else:
      print('Tijera gana a papel')
      print('GANA LA COMPUU')
      computer_wins += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('GANA EL USER!')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('GANA LA COMPUU')
      computer_wins += 1

  if computer_wins == 2:
    print('EL GANADOR ES LA COMPUTADORA')
    break

  if user_wins == 2:
    print('EL GANADOR ES EL USER!')
    break
