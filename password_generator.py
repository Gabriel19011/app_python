def new_password():
    import random
    while True:
        scale = int(input("\n\nDigite o tamanho da sua nova senha:"))
        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_character = "!@#$%^&*()."
        string = lower_letters + upper_letters + numbers + special_character
        password = "".join(random.sample(string, scale))
        # print('Your new password is :' + password)
        x='=-'*30
        print(f"\n\nSua nova senha:\n{x}\n\n{password}\n\n{x}")
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            if resp in 'SN':
                break
            print('ERRO! Responda apenas S ou N.')
        if resp == 'N':
            print('Parando sistema')
            break
new_password()