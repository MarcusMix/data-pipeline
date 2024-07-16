import pandas as pd

nome = "3jul_apple_star2" + ".json"

path_completo = f"/home/winker/Documentos/webscraping-googleplaystore-assessment-main/googlewebscraping/data/{nome}"
path_csv = "/home/winker/Documentos/webscraping-googleplaystore-assessment-main/googlewebscraping/csv/"

df = pd.read_json(path_completo)

print(df)

df.to_csv(path_csv + "AGORAjul_apple_star-tratado.csv", index=False)