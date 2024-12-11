import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests

#tela da interface
class MainView(tk.Tk):
    def __init__(self):
        # heranca
        super().__init__()

        # tamanho e titulo
        self.title("Cliente DNS")
        self.geometry("400x500")

        # Area de texto para entrada do endereco DNS
        self.label_message = tk.Label(self, text="Endereço DNS:")
        self.label_message.pack(padx=5, pady= 5)

        self.message_entry = tk.Text(self, height=3)
        self.message_entry.pack(padx=10, pady=5, fill=tk.X)

        #variavel opcao e opcoes que tem no optionMenu
        opcaoSelecionada = tk.StringVar()
        opcaoSelecionada.set("A")
        opcoes = ["A","AAAA", "MX"]

        # Criar a OptionMenu e botao de pesquisar
        menu_opcoes = tk.OptionMenu(
            self,
            opcaoSelecionada,
            *opcoes,  # Desempacota a lista de opções
        )
        menu_opcoes.pack(padx=5, pady= 5)

        self.send_button = tk.Button(self, text="pesquisar", command=self.searchDNS)
        self.send_button.pack(padx=5, pady=5)

        # Saida de informações do cliente DNS
        self.chat_area = ScrolledText(self, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=5, pady= 5)

    def searchDNS(self):
        link = self.message_entry.get("1.0", tk.END).strip()
        response = requests.get(link)

        if response:
            # Habilita a area de chat para editar
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, response.json()['ip']) #edita
            self.chat_area.config(state='disabled')  # Desabilita para edição
            self.chat_area.yview(tk.END)  # Rola para o fim

            # Limpa a área de entrada
            self.message_entry.delete("1.0", tk.END)
        else:
            # Habilita a area de chat para editar
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, "endereço não encontrado") #edita
            self.chat_area.config(state='disabled')  # Desabilita para edição
            self.chat_area.yview(tk.END)  # Rola para o fim

            # Limpa a área de entrada
            self.message_entry.delete("1.0", tk.END)



#inicia a aplicacao
if __name__ == "__main__":
    app = MainView()
    app.mainloop()