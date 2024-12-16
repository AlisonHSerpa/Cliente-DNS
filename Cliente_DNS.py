import tkinter as tk
from tkinter import ttk
import requests

class DNSClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente DNS")

        # Inicia a interface
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Entrada do domínio
        self.domain_label = ttk.Label(self.frame, text="Dominio:")
        self.domain_label.grid(row=0, column=0, sticky=tk.W)
        self.domain_entry = ttk.Entry(self.frame, width=30)
        self.domain_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

        # OptionMenu para o tipo de registro
        self.record_type_label = ttk.Label(self.frame, text="Tipo de Registro:")
        self.record_type_label.grid(row=1, column=0, sticky=tk.W)
        self.record_type = tk.StringVar(value="A")
        self.record_type_menu = ttk.OptionMenu(
            self.frame, self.record_type, "A", "A", "AAAA", "CNAME", "MX", "NS", "TXT"
        )
        self.record_type_menu.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Botão para consulta
        self.query_button = ttk.Button(self.frame, text="Consultar", command=self.query_dns)
        self.query_button.grid(row=2, column=0, columnspan=3, pady=10)

        # TextArea para a saída
        self.result_text = tk.Text(self.frame, wrap="word", height=15, width=60)
        self.result_text.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))
        self.result_text.configure(state="disabled")

        # Configuração de espaçamento
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # Faz a consulta DNS e exibe o resultado na área de texto
    def query_dns(self):
        # Domínio e tipo
        domain = self.domain_entry.get().strip()
        record_type = self.record_type.get()

        # Se não tiver domínio, pede para escrever
        if not domain:
            self.display_result("Por favor, insira um domínio...")
            return

        url = "https://dns.google/resolve"
        params = {"name": domain, "type": record_type}

        # Faz a pesquisa do domínio
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Prepara o cabeçalho da resposta
            header = (
                f"Consulta DNS:\n"
                f"- Domínio: {domain}\n"
                f"- Tipo de Registro: {record_type}\n\n"
                f"Resultados:\n"
            )

            if "Answer" in data:
                # Trata os registros encontrados
                results = []
                for item in data["Answer"]:
                    name = item.get("name", "N/A")
                    record_data = item.get("data", "N/A")
                    results.append(f"  {name} -> {record_data}")

                self.display_result(header + "\n".join(results))
            else:
                # Sem resposta na consulta
                self.display_result(header + "Nenhum registro encontrado.")

        except requests.RequestException as e:
            self.display_result(f"Erro ao consultar DNS: {e}")

    # Exibe uma mensagem na TextArea
    def display_result(self, message):
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message)
        self.result_text.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = DNSClientApp(root)
    root.mainloop()
