import requests as rq
import json as js
import pandas as pa
import matplotlib as mpl
import xgboost as xg
import numpy as np
import os
import tabulate as tb
import statsmodels as sm
import time
import yfinance as yf


def main():
  fetch_gold_dict()




def fetch_gold_dict():
  gp_data = yf.Ticker("GC=F")
  gp_history = gp_data.history(period="1y")
  gp_history_to_dict = gp_history.to_dict()
  print(gp_history_to_dict)


if __name__ == "__main__":
  main()
  