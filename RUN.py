import subprocess
import sys

# This uses system terminal to install python modules
subprocess.call([sys.executable, "-m", "pip", "install", 'xlrd'])
subprocess.call([sys.executable, "-m", "pip", "install", 'XlsxWriter'])

import os
import xlrd as xread
import xlsxwriter as xwrite
from Classes import SerialEntrepreneur


def init():
    # opening database file
    database_loc = os.path.join(sys.path[0], 'database.xlsx')
    print(database_loc)
    try:
        database_wb = xread.open_workbook(database_loc)
        database_sheet = database_wb.sheet_by_index(0)
    except:
        print("\n" + "Error: No Excel Sheet Named 'database.xlsx' Found :( ")
        input("Please paste the database sheet into this folder, and run the script again!")

    # creating diagnostic sheets
    file_loc = os.path.join(sys.path[0], 'UC Berkeley Serial Entrepreneurs.xlsx')
    data_wb = xwrite.Workbook(file_loc)
    data_sheet = data_wb.add_worksheet('Data')

    # sheet formats
    bold = data_wb.add_format({'bold': True, 'font_color': 'red'})

    # turning database into data
    people = make_person(database_sheet)

    # PERFORMING ANALYSIS
    # identifying serial entrepreneurs
    serial_entrepreneurs = find_serial_entrepreneurs(people, bold)

    print("Found " + str(len(serial_entrepreneurs)) + " serial entrepreneurs!")
    data_wb.close()

    # exit
    input("\n" + "Completed! Press any key to exit... ")
    exit()


def make_person(sheet):
    # status
    print("\n" + "Making People...")

    people = []

    for i in range(1, sheet.nrows):
        if sheet.cell_value(i, 0) != "":
            id = sheet.cell_value(i, 0)
            full_name = sheet.cell_value(i, 1)
            last_name = sheet.cell_value(i, 2)
            first_name = sheet.cell_value(i, 3)
            primary_position = sheet.cell_value(i, 4)
            primary_company = sheet.cell_value(i, 5)
            board_seats = sheet.cell_value(i, 6)
            roles = sheet.cell_value(i, 7)
            deal_roles = sheet.cell_value(i, 8)
            phone = sheet.cell_value(i, 9)
            email = sheet.cell_value(i, 10)
            location = sheet.cell_value(i, 11)
            address_line1 = sheet.cell_value(i, 12)
            address_line2 = sheet.cell_value(i, 13)
            city = sheet.cell_value(i, 14)
            state = sheet.cell_value(i, 15)
            post_code = sheet.cell_value(i, 16)
            country = sheet.cell_value(i, 17)
            fax = sheet.cell_value(i, 18)
            biography = sheet.cell_value(i, 19)
            pitchbook_link = sheet.cell_value(i, 20)

            new_serial_entrepreneur = SerialEntrepreneur(id, full_name, last_name, first_name,
                                                         primary_position, primary_company, board_seats,
                                                         roles, deal_roles, phone, email, location,
                                                         address_line1, address_line2, city, state,
                                                         post_code, country, fax, biography, pitchbook_link)
            people.append(new_serial_entrepreneur)

            # status
            print(new_serial_entrepreneur.full_name + "|| completed")

    return people


def find_serial_entrepreneurs(people, style, i=0):
    # status
    print("\n" + "Finding Serial Entrepreneurs" + "\n")

    serial_entrepreneurs = []
    unique_persons = {}

    # check if a founder is a serial entrepreneur
    for person in people:
        if person.ID not in unique_persons:
            unique_persons[person.ID] = person.full_name
        else:
            print("Serial Entrepreneur: " + person.full_name)
            serial_entrepreneurs.append(person)
            i += 1

    return serial_entrepreneurs


init()