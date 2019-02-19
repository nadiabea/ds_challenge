import numpy as np
import pandas as pd
import pandas_profiling

aw_data = pd.read_csv("ds_challenge_adwords.csv")
fb_data = pd.read_csv("ds_challenge_facebook.csv")

pandas_profiling.ProfileReport(aw_data)
pandas_profiling.ProfileReport(fb_data)
