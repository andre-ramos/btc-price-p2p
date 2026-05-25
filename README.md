# btc-price-p2p

This project is a small Bitcoin P2P price monitor focused on the Brazilian market. It fetches the current BTC/BRL reference price, compares it against [HODL HODL](https://hodlhodl.com/) buy offers, and sends Telegram alerts when it finds listings inside a price threshold.

## What it does

- Fetches the current Bitcoin BRL price from `awesomeapi.com.br`
- Queries [HODL HODL](https://hodlhodl.com/) offers in BRL
- Filters sellers by trade history and price
- Sends Telegram notifications for interesting offers

## Why I built it

This repo was an experiment in spotting better-than-average peer-to-peer Bitcoin offers and automating the alerting step instead of checking marketplaces manually.

## Main files

- `fetch_p2p_price.py`: pulls prices, filters offers, and sends Telegram messages

## Tech

- Python
- Requests
- Telegram Bot API

## Notes

The script expects secrets such as `BOT_KEY` and `API_KEY` to be provided through environment variables.
