import requests as rq
import json as js
import pandas as pd
import matplotlib as mpl
import xgboost as xg
import numpy as np
import os
import tabulate as tb
import statsmodels as sm
import time
import yfinance as yf


def main():
  fetch_gold_dataframe()




def fetch_gold_dataframe():
  gp_data = yf.Ticker("GC=F")
  gp_df = gp_data.history(period="5y")

  gp_df["Open"].plot(title="Gold Price")
  mpl.pyplot.show()


if __name__ == "__main__":
  main()
  