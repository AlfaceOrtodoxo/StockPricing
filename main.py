import yfinance as yf
import openpyxl as opxl
import time
import keyboard
import os

dir_script = os.path.dirname(os.path.abspath(__file__))

os.chdir(dir_script)

pasta = opxl.load_workbook("wallet.xlsx")
carteira = pasta['wallet']

def main():
    while True:
        cotacao()
        time.sleep(3)
        limpar_terminal()
        if keyboard.is_pressed('esc'):
            break
    input('Pressione "enter" para sair...')


def cotacao():
    for cell in carteira['A']:
        ticker = cell.value
        if ticker is not None:  # Verifica se o ticker não é None
            try:
                price = yf.Ticker(ticker).history(period="1d")['Close'].iloc[0]
                print('{}: R$ {:.2f}'.format(ticker, price))
            except Exception as e:
                print(f"Erro ao obter o preço para {ticker}: {e}")

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')


if __name__ == "__main__":
    main()
    



