from logging import exception
import time
import gspread
import do_requests as api
from gspread_dataframe import set_with_dataframe

'''NOTAS: los workbook tienen un limite de 10M cells, y si esto se supera nos lanza este error:
NOK - Algo salio mal: {'code': 400, 'message': 'Invalid requests[0].updateSheetProperties: This action would increase the number of cells in the workbook above the limit of 10000000 cells.', 'status': 'INVALID_ARGUMENT'}
'''
gc = gspread.service_account(filename='cotest-338402-5cfff347c4f7.json')

# Abro mi planilla gsheet
worksheet = gc.open("CO_Test")

# Obtengo de la API request la info en dataframe
CO_list = api.get_CO_list()

# Especifico la fecha y ahora de la descarga
str_time = time.strftime("%Y-%m-%d_%H.%M.%S")

# Creo una nueva sheet con la fecha de la descarga y con set_with_dataframe la lleno con los valores
try:
    worksheet.add_worksheet(title=f'CO_{str_time}', rows=1, cols=1)
    set_with_dataframe(worksheet.worksheet(f'CO_{str_time}'), CO_list)
    id_worksheet = worksheet.worksheet(f'CO_{str_time}').id
    print(
        f"OK - Se completo el proceso, link https://docs.google.com/spreadsheets/d/1pARHTSCtVEPMdIWfM_TsgzdxyYwUoVLULpH9Rq7DYRo/edit#gid={id_worksheet}")
except Exception as e:
    print(f"NOK - Algo salio mal: {e}")
