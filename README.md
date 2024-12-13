# Cliente DNS com Interface Gráfica (Tkinter)

Este é um cliente DNS simples com interface gráfica construída em Python utilizando Tkinter. Ele permite realizar consultas DNS com facilidade, diretamente de uma interface amigável.

## Requisitos

Antes de começar, certifique-se de atender aos seguintes requisitos:
- **Python 3.13 ou superior** instalado em sua máquina.
- A biblioteca `requests` instalada.

## Instruções de Instalação e Deploy

Siga os passos abaixo para instalar e executar o programa:

1. **Verifique sua versão do Python**:
   Certifique-se de que o Python está instalado e na versão 3.13 ou superior. No terminal (ou CMD), execute:
   ```bash
   python --version
   ```
   Caso não tenha o Python instalado, faça o download em [python.org](https://www.python.org/).

2. **Instale a biblioteca `requests`**:
   - Abra o terminal (ou CMD) e digite:
     ```bash
     pip install requests
     ```
   - Para verificar se a instalação foi bem-sucedida, use:
     ```bash
     pip freeze
     ```
     O nome `requests` deve aparecer na lista. Caso contrário, tente reinstalar.

3. **Baixe o projeto**:
   - Faça o download do arquivo ZIP do projeto.
   - Extraia os arquivos para um diretório de sua escolha.

4. **Acesse o diretório do projeto**:
   - No terminal (ou CMD), navegue até a pasta do projeto:
     ```bash
     cd /caminho/para/o/projeto
     ```

5. **Execute o programa**:
   - No terminal (ou CMD), execute o seguinte comando:
     ```bash
     python cliente_DNS.py
     ```

## Exemplo de Uso

1. Insira o domínio no campo de texto (ex.: `example.com`).
2. Escolha o tipo de registro DNS no menu suspenso (ex.: `A`, `MX`).
3. Clique em "Consultar" para visualizar os resultados.

## Observações

- Este projeto utiliza a API pública do Google DNS-over-HTTPS para realizar as consultas DNS.
- Certifique-se de estar conectado à internet ao executar o programa.
- Caso encontre erros, verifique os passos acima e certifique-se de que o Python e as dependências estão instalados corretamente.
