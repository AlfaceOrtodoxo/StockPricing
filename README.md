# Stock Price Monitor

This Python script monitors and displays the stock prices listed in an Excel spreadsheet (`wallet.xlsx`). The prices are updated in real-time and displayed in the terminal. The script will keep running until the `Esc` key is pressed.

## Requirements

- Python 3.x
- Python Libraries:
  - `yfinance`
  - `openpyxl`
  - `keyboard`

You can install the required libraries using `pip`:

```bash
pip install yfinance openpyxl keyboard
```

## Setup

1. Make sure the `wallet.xlsx` file is located in the same directory as the script.
2. The `wallet.xlsx` file should contain a worksheet named `wallet` with the stock tickers listed in column `A`.

## How to Use

1. Run the script in your terminal or development environment:

```bash
python main.py
```

2. The script will display the stock prices in real-time. To stop the monitoring, press the `Esc` key.
3. After the monitoring ends, press `Enter` to exit the program.

## Features

- **Continuous Updates:** Prices are updated every second.
- **Price Display:** The closing prices of the stocks are displayed in the format `Ticker: $ Price`.
- **Manual Stop:** Press `Esc` at any time to stop the script.

## Notes

- This script was developed for Windows environments (`os.name == 'nt'`). If you are using a different operating system, you will need to adjust the terminal clearing function.

## License

This project is licensed under the terms of the MIT License.
