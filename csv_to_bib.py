import sys
import csv
from os import listdir
from os.path import isfile, join, dirname, realpath
from time import sleep
from os import remove


def find_all_files(mypath = dirname(realpath(__file__))):
    """
    Function that returns a list with the names of all the file_type files
    """
    file_type = ".csv"
    mypath = dirname(realpath(__file__))
    all_files_in_path = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    chosen_files = []
    for i in range(len(all_files_in_path)):
        if all_files_in_path[i].endswith(file_type):
            chosen_files.append(all_files_in_path[i])
    return(chosen_files)

def read_files(list_of_files):
    all_data = []
    all_names = []
    for arquivo in range(len(list_of_files)):
        filename = list_of_files[arquivo]
        dataArray = []
        count = 0
        with open(filename,'r') as csvfile:
            """
            When first line of CSV is composed of keys has_key must be true
            """
            has_key = iskey = True
            keys = []
            reader = csv.reader(csvfile,delimiter=';')
            for row in reader:
                if iskey:
                    keys = row
                    iskey = False
                    keys = [k for k in keys if k!='']
                else:
                    clean_dataframe = {}
                    rowArr = row
                    for i in range(len(keys)):
                        clean_dataframe[str(keys[i])] = str(rowArr[i])
                    clean_dataframe["ide"] = count
                    count = count+1
                    dataArray.append(clean_dataframe)
            print("HiFILE")
        list_of_files[arquivo] = list_of_files[arquivo][:-4]
        nome_arquivo = list_of_files[arquivo] + ".bib"
        all_data.append(dataArray)
        all_names.append(nome_arquivo)
    return([all_data, all_names])

def generate_data(data_array, file_name):
    with open(file_name,"w") as outfile:
        to_print = ''
        # Usando:
        # - Instituto
        # - Tipo
        # - Sigla
        # - Documento
        # - Keywords
        try:
            print(file_name)
            for data in data_array:
                # data['Keywords'] = data['Keywords'].replace(',','; ').replace(', ', '; ')
                # to_print += ('\n@ARTICLE{mctic'+str(data['ide'])+',\n')
                # to_print += ('author={'+data['Tipo']+'},\n')
                # to_print += ('title={'+data['Instituto']+'},\n')
                # to_print += ('journal={'+data['Sigla']+'},\n')
                # to_print += ('year={2017},\n')
                # to_print += ('doi={'+str(data['ide'])+'},\n')
                # to_print += ('abstract={'+data['Documento']+'},\n')
                # to_print += ('language={Brazilian Portuguese},\n')
                # to_print += ('document_type={Article},\n')
                # to_print += ('keywords={' + data['Keywords'] + '},\n')
                # to_print += ('source={Scopus},\n}\n')
        except Exception as e:
            print("Error: " + str(e))
            with open("error.txt","w") as erros:
                erros.write(str(e))
            sleep(5)
            outfile.close()
            remove(data_array)
            return(-1)
        outfile.write(to_print)
    return(to_print)

if __name__ == "__main__":
    files = find_all_files()
    print(files)
    dados, nome_arquivos = read_files(files)
    for posicao in range(len(dados)):
        generate_data(dados[posicao], nome_arquivos[posicao])
