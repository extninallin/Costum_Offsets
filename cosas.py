#########################################################################

# for file in csv_list:
#     path_to_file = os.path.join(directory, file)
#     lista = []
#     name_ws = []
#     name_ws.append(file)
#     # print(name_ws)
#     lista.append(path_to_file)


# if len(csv_list) >= 3:
#     for file in csv_list:
#         path_to_file = os.path.join(directory, file)
#         lista = []
#         lista.append(path_to_file)
#         print(lista)

#     filtered_files.clear()
#     csv_list.clear()
#     os.remove(lista[0])
#     #os.remove(path_to_file)
# local_directory = os.getcwd()  # getcwd obtengo mi directorio actual parado
# local_directory = pathlib.PureWindowsPath(os.getcwd())  # getcwd obtengo mi directorio actual parado
# local_directory.as_posix()

# df = pd.DataFrame(worksheet.sheet1.get_all_records())
# csv_list = []
# print(csv_list)


# # Guardo el get del request en un .csv para luego importarlo en el gsheet
# CO_list.to_csv(
#     f"CO_list_{str_time}.csv", encoding='utf-8', index=False)


# # busco en mi directorio local todos los archivos csv
# directory = local_directory

# con listdir obtengo todo lo que hay en el directorio y luego lo filtro por endswith
# files_in_directory = os.listdir(directory)
# filtered_files = [file for file in files_in_directory if file.endswith(".csv")]


# # Aca guardo en una lista todos los nombres de los .csv que encontre
# for item in range(0, len(filtered_files)):
#     csv_list.append(filtered_files[item])

# csv_list.sort()
# print(csv_list)


# worksheet.add_worksheet(title=f'{csv_list[-1]}',rows=100,cols=100)
# set_with_dataframe(worksheet.worksheet(f'{csv_list[-1]}'),CO_list)

# Abro el archivo momentaneamente y lo leo con un read, luego lo importo al gsheet
# with open(csv_list[-1], 'r', encoding='utf-8') as file_obj:
#     content = file_obj.read()
#     gc.import_csv(worksheet.id, data=content.encode('utf-8'))
#     worksheet.sheet1.update_title(f'{csv_list[-1]}')
#########################################################################
