def ValidaCpf(msg='Cadastro de Pessoa Física (CPF): ', pont=True):
    """
    -> Função para validar um CPF
    :param msg: Mensagem exibida para usuário antes de ler o CPF.
    :param pont: Se True, retorna um CPF com pontuação (ex: xxx.xxx.xxx-xx).
        Se False, retorna um CPF sem pontuação (ex: xxxxxxxxxxx)
    :return: Retorna um CPF válido.
    """
    while True:
        cpf = str(input(f'{msg}'))
        if '.-' in cpf and pont == False:
            cpf.replace('.', '')
            cpf.replace('-', '')
        contDig=0
        for dig in cpf:
            if dig.isnumeric():
                contDig += 1 # Conta a quantidade de dígitos no CPF

        if contDig != 11: # Se o CPF possuir mais de 11 dígitos, retorna uma mensagem de erro
            print('\033[1;31m3RRO! Este CPF é inválido!\033[m')
            continue # Volta para o tpo do laço

        if '.' in cpf: # Verifica a existência de pontos no CPF e se a quantidade está correta(2)
            if cpf.count('.') != 2:
                print('\033[1;31m3RRO! Este CPF é inválido!\033[m')
                continue
        else: # Se não tiver pontos e se pont=True, adiciona a pontuação
            if pont:
                cpf = list(cpf)
                cpf.insert(3, '.')
                cpf.insert(7, '.')

        if '-' in cpf: # Verifica a existência do hífen no CPF e se a quantidade está correta(1)
            if cpf.count('-') != 1:
               print('\033[1;31m3RRO! Este CPF é inválido!\033[m')
               continue
        else: # Se não tiver hífen e se pont=True, adiciona a pontuação
            if pont:
                cpf.insert(11, '-')

        result = [''.join(cpf)] # Junta a lista
        cpf = result[0] 
        break
    return cpf


cpf = ValidaCpf(msg='CPF: ', pont=True)
print(cpf)
help(ValidaCpf) # Exibe a DocString da função
