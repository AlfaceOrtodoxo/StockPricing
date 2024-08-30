import yfinance as yf
import openpyxl as opxl
import time
import keyboard
import os
import datetime as dt

dir_script = os.path.dirname(os.path.abspath(__file__))

os.chdir(dir_script)

workbook = opxl.load_workbook("wallet.xlsx")
wallet = workbook['wallet']



def main():
    while True:
        format()
        time.sleep(1)
        clearTerminal()
        if keyboard.is_pressed('esc'):
            break
    format()
    input('Pressione "enter" para sair...')


def pricing():
    for cell in wallet['A']:
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

def format():
    hour = dt.datetime.now()
    print('=====================')
    print(hour.strftime("%d-%m-%Y - %H:%M:%S"))
    print('=====================')
    pricing()
    print('=====================')

def clearTerminal():
    if os.name == 'nt':
        os.system('cls')


if __name__ == "__main__":
    main()
    



