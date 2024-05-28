from interface.csv_class import CsvProcessor
# import pandas as pd

arquivo_csv = "./exemplo.csv"
# filtro = "Produto"
# produto = "Notebook Gamer"
      
csv_final = CsvProcessor(arquivo_csv)
csv_final.carregar_csv()

print(csv_final.filtrar_por(["Produto"] , ["Notebook Gamer"]))
# print(csv_final.filtrar_por(["Produto", "Data"] , ["Notebook Gamer", "2023-01-15"]))



# arquivo_csv2 = './examplo2.csv'

# csv_final2 = CsvProcessor(arquivo_csv2)
# csv_final2.carregar_csv()  # Load the CSV
# print(csv_final.filtrar_por(["Produto", "Data"] , ["Notebook Gamer", "2023-01-15"]))
