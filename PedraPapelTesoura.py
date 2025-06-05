#BEM VINDO AO JOGO PEDRA, PAPEL E TESOURA!
import random

user_points = 0
computer_points = 0
options = ["r", "t", "p"]

while True:
    user_choice = input("\nEscolha R (PEDRA) / T (TESOURA) / P (PAPEL) \nDigite Q para sair.").lower()
    if user_choice == 'q':
        break
    if user_choice not in options:
        print("Escolha inválida. Tente novamente.")
        continue

    computer_choice = random.randint(0, 2)
    #0 = R / 1 = T / 2 = P

    computer_option = options[computer_choice]
    print("Eu escolhi: " + options[computer_choice] )

    if user_choice == computer_option:
        print("Empate!")

    elif user_choice == 'r' and computer_option:
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == 'p' and computer_option == 'r':
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == 't' and computer_option == 'p':
        print("Você ganhou!")
        user_points = user_points + 1

    else:
        computer_points = computer_points + 1
        print("Você perdeu haha")


print(f"\nFIM DE JOGO! \nPLACAR FINAL = EU {computer_points} x Você {user_points} ")
if user_points > computer_points:
    print("Parabéns vc venceu...")
if user_points == computer_points:
    print("EMPATAMOS")
elif user_points < computer_points:
    print("Você perdeu HAHAHAHAHAHA")