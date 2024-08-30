import yfinance as yf
import openpyxl as opxl
import time
import keyboard
import os
import datetime as dt

dir_script = os.path.dirname(os.path.abspath(__file__))

os.chdir(dir_script)

pasta = opxl.load_workbook("wallet.xlsx")
carteira = pasta['wallet']



def main():
    while True:
        hour = dt.datetime.now()
        print('=====================')
        print(hour.strftime("%d-%m-%Y - %H:%M:%S"))
        print('=====================')
        cotacao()
        print('=====================')
        time.sleep(1)
        limpar_terminal()
        if keyboard.is_pressed('esc'):
            break
    input('Pressione "enter" para sair...')


def cotacao():
    for cell in carteira['A']:
        ticker = cell.value
        if ticker is not None:
            try:  
                price = yf.Ticker(ticker).history(period="1d")['Close'].iloc[0]
                if ".SA" in ticker:
                    print('{}:       R$ {:.2f}'.format(ticker[0:5], price))
                else:
                    print('{}:      US$ {:.2f}'.format(ticker, price))
            except Exception as e:
                print(f"Erro ao obter o preço para {ticker}: {e}")

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')


if __name__ == "__main__":
    main()
    



