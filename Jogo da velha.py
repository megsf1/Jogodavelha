class JogoDaVehla:
    tabuleiro = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
    turno = None

    def _init_(self, jogador_inicial="X"):
        self.turno = jogador_inicial

    def exibir_tabuleiro(self):
        print("MANUAL DE POSIÇÕES")
        print("┌───┬───┬───┐")
        print("│ 1 │ 2 │ 3 │")
        print("├───┼───┼───┤")
        print("│ 4 │ 5 │ 6 │")
        print("├───┼───┼───┤")
        print("│ 7 │ 8 │ 9 │")
        print("└───┴───┴───┘")

        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("└───┴───┴───┘")

    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    def verificar_tabuleiro(self):
        
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']


        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']

        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']

        
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.tabuleiro.values()].count(' ')

    def jogar(self):

        while True:
            self.exibir_tabuleiro()

            print(f"Turno do {self.turno}, qual sua jogada?")

            
            while True:
                jogada = input("Jogada: ")

                if self.verificar_jogada(jogada):  
                    break  
                else:
                    print(f"jogado do {self.turno} inválida, jogue novamente.")

            self.tabuleiro[jogada] = self.turno

            estado = self.verificar_tabuleiro()

            if estado == "X":
                print("X é o vencedor!!!")
                break

            elif estado == "O":
                print("O é o vencedor!!!")
                break

            if estado == "empate":
                print("EMPATE!!!")
                break

            
            self.turno = "X" if self.turno == "O" else "O"

        self.exibir_tabuleiro()
