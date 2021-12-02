import openpyxl

# filename path
filename = "/Users/Dev/Code/Git_Repositories/VetsInTech/Python Fundamentals/1121-itp/itp_week_3/day_3/lecture.xlsx"


# load workbook
my_workbook = openpyxl.load_workbook(filename)

# get list of sheet names
sheet_list = my_workbook.get_sheet_names()

print(sheet_list)

my_sheet = my_workbook.get_sheet_by_name('Sheet1')

my_sheet["A8"] = "YOU'VE"
my_sheet["B8"] = "BEEN"
my_sheet["C8"] = "HACKED"

filename_copy = "/Users/Dev/Code/Git_Repositories/VetsInTech/Python Fundamentals/1121-itp/itp_week_3/day_3/lecture_test_save.xlsx"

my_workbook.save(filename_copy)