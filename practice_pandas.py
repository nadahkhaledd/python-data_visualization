import matplotlib.pyplot as plt
import pandas as pd

raw_data = {'names': ['Nick', 'Jessie', 'Robin', 'Marc', 'Jimmy'],
            'jan_ir': [143, 122, 101, 106, 365],
            'feb_ir':[122, 132, 144, 98, 621],
            'march_ir': [65, 88, 12, 32, 65]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])
print(df)


