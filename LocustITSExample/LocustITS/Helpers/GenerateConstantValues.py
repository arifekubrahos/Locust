import pandas
import numpy as np
import xlrd
from random import choice
#if you want to show table add  "iDisplayStart":"0","iDisplayLength":"10"


class ITSConstantValues():

    def create_gtin_sn(self):

        matrix = pandas.read_excel("\gtin-sn.xlsx").as_matrix()
        array = matrix[np.random.randint(matrix.shape[0], size=1), :]
        array = {"gtin": "0" + str(array[0][0]), "sn": array[0][1]}

        return array

    def create_sn(self):

         excel = xlrd.open_workbook("\sn.xlsx")
         excelsheet = excel.sheet_by_index(0)
         sn = {"sn":str(int(choice(excelsheet.col(0)).value))}

         return sn

    def create_gtin(self):

        excel = xlrd.open_workbook("\gtin.xlsx")
        excelsheet = excel.sheet_by_index(0)
        gtin = {"gtin":"0"+str(int(choice(excelsheet.col(0)).value))}

        return gtin

    def create_gln(self):

        excel = xlrd.open_workbook("\gln.xlsx")
        excelsheet = excel.sheet_by_index(0)
        gln = {"gln":str(int(choice(excelsheet.col(0)).value))}

        return gln

    def create_pres_id(self):

        array = pandas.read_excel("\prescription_record_number.xlsx")
        array = {"_pres_record_number": array}

        return array

    def create_notification_id(self):

        array = pandas.read_excel("\\notificationID.xlsx")
        array = {"notificationId": array}

        return array