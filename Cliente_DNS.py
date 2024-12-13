import tkinter as tk
from tkinter import ttk
import requests

class DNSClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente DNS")

        #inicia a interface
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        #Entrada do domínio
        self.domain_label = ttk.Label(self.frame, text="Dominio:")
        self.domain_label.grid(row=0, column=0, sticky=tk.W)
        self.domain_entry = ttk.Entry(self.frame, width=30)
        self.domain_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

        #OptionMenu para o tipo de registro
        self.record_type_label = ttk.Label(self.frame, text="Tipo de Registro:")
        self.record_type_label.grid(row=1, column=0, sticky=tk.W)
        self.record_type = tk.StringVar(value="A")
        self.record_type_menu = ttk.OptionMenu(
            self.frame, self.record_type, "A", "A", "AAAA", "CNAME", "MX", "NS", "TXT"
        )
        self.record_type_menu.grid(row=1, column=1, sticky=(tk.W, tk.E))

        #Botao para consulta
        self.query_button = ttk.Button(self.frame, text="Consultar", command=self.query_dns)
        self.query_button.grid(row=2, column=0, columnspan=3, pady=10)

        #TextArea pra a saida
        self.result_text = tk.Text(self.frame, wrap="word", height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))
        self.result_text.configure(state="disabled")

        # Configuração de espaçamento
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    #Faz a consulta DNS e exibe o resultado na área de texto
    def query_dns(self):
        #Dominio e tipo
        domain = self.domain_entry.get().strip()
        record_type = self.record_type.get()

        #se nao tiver dominio, pede pra escrever
        if not domain:
            self.display_result("Por favor, insira um dominio...")
            return

        url = "https://dns.google/resolve"
        params = {"name": domain, "type": record_type}
        
        #faz a pesquisa do dominio
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            if "Answer" in data:
                results = "\n".join(f"{item['name']} {item['type']} {item['data']}" for item in data["Answer"])
                self.display_result(f"Resultados para {domain} ({record_type}):\n{results}")
            else:
                self.display_result(data.get("Comment", "Nenhum registro encontrado."))

        except requests.RequestException as e:
            self.display_result(f"Erro ao consultar DNS: {e}")

    #Exibe uma mensagem na textArea
    def display_result(self, message):
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message)
        self.result_text.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = DNSClientApp(root)
    root.mainloop()
