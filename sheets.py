import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import numpy as np
from pyanp import priority

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("MyStrefa.json", scope)

client = gspread.authorize(creds)

sheet = client.open("formularzkibic").sheet1  # Open the spreadhseet


# DATA SETS


def revalue(list):
    for e in range(len(list)):
        if list[e] == 5:
            list[e] = 1
        elif list[e] == 4:
            list[e] = 1/3
        elif list[e] == 6:
            list[e] = 3
        elif list[e] == 3:
            list[e] = 1/5
        elif list[e] == 7:
            list[e] = 5
        elif list[e] == 2:
            list[e] = 1/7
        elif list[e] == 8:
            list[e] = 7
        elif list[e] == 1:
            list[e] = 1/9
        else:
            list[e] = 9
    return list


def fill_matrix(list, matrix):
    for e in list:
        for i in range(len(matrix)):
            find = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = e
                    matrix[j][i] = 1 / e
                    find = True
                    break
            if find:
                break
    return matrix


# loading range data from sheet


data_range = sheet.range('B3:AC3')

# preferencje kryteriów głównych dla grupy kibic pkgk
pkgk = []
for c in data_range[0:3]:
    pkgk.append(int(c.value))

# preferencje dojazd dla grupy kibic pdk
pdk = []
for c in data_range[3:6]:
    pdk.append(int(c.value))

# preferencje udogodnień dla grupy kibic puk
puk = []
for c in data_range[6:12]:
    puk.append(int(c.value))

# preferencje gastronomia dla grupy kibic pgk
pgk = []
for c in data_range[12:18]:
    pgk.append(int(c.value))

# preferencje lokalizacja dla grupy kibic plk
plk = []
for c in data_range[18:28]:
    plk.append(int(c.value))

x = 3

while True:

    matrix_pkgk = np.zeros((len(pkgk), len(pkgk)), float)
    np.fill_diagonal(matrix_pkgk, 1)
    fill_matrix(revalue(pkgk), matrix_pkgk)
    print("pkgk:", matrix_pkgk)

    matrix_pdk = np.zeros((len(pdk), len(pdk)), float)
    np.fill_diagonal(matrix_pdk, 1)
    fill_matrix(revalue(pdk), matrix_pdk)
    print("pdk:", matrix_pdk)

    matrix_puk = np.zeros((len(puk), len(puk)), float)
    np.fill_diagonal(matrix_puk, 1)
    fill_matrix(revalue(puk), matrix_puk)
    print("puk:", matrix_puk)

    matrix_pgk = np.zeros((len(pgk), len(pgk)), float)
    np.fill_diagonal(matrix_pgk, 1)
    fill_matrix(revalue(pgk), matrix_pgk)
    print("pgk:", matrix_pgk)

    matrix_plk = np.zeros((len(plk), len(plk)), float)
    np.fill_diagonal(matrix_plk, 1)
    fill_matrix(revalue(plk), matrix_plk)
    print("plk:", matrix_plk)

    x +=1
    data_range = sheet.range('B'+str(x)+':AC'+str(x))
    if data_range[0].value == '':
        break

    pkgk = []
    for c in data_range[0:3]:
        pkgk.append(int(c.value))

    pdk = []
    for c in data_range[3:6]:
        pdk.append(int(c.value))

    puk = []
    for c in data_range[6:12]:
        puk.append(int(c.value))

    pgk = []
    for c in data_range[12:18]:
        pgk.append(int(c.value))

    plk = []
    for c in data_range[18:28]:
        plk.append(int(c.value))

