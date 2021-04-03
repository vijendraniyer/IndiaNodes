# Writing to an excel 
# sheet using Python
import pandas as pd
from xlwt import Workbook

pd.set_option("display.max_rows", None, "display.max_columns", None)
df_edges = pd.read_excel('graph.xlsx', sheet_name='Edges')

row_values = []
states_and_borders = []
for primary in df_edges.iterrows():
    for name in primary[1]:
        if not pd.isna(name):
            row_values.append(name.strip())
    if len(row_values):
        states_and_borders.append(row_values[:])
    row_values.clear()

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Nodes&Edges')

row = 0
col = 1
for i in states_and_borders:
    for j in range(col, len(i)):
        sheet1.write(row, not col, i[0])
        sheet1.write(row, col, i[j])
        row += col

wb.save('graph.xls')
