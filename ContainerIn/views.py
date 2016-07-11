from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import openpyxl
# Create your views here.

@login_required
def ContainerFormer(request):
    return render(request, "Forms.html")

wb = openpyxl.load_workbook('IMPORT DATA.xlsx')
sheet = wb.get_sheet_by_name('JUNE 2016')
VSL_NAME = []
VOY= []
TERMINAL=[]
IGM_NO=[]
IGM_DATE=[]
ACCOUNT =[]
CONTAINER_NO=[]
SIZE = []
STATUS = []
ICD_LOCAL=[]
POD = []
DISCHARGE_DATE= []
RAIL_ROUD_OUT = []
EMPTY_IN=[]
YARD= []
for row in range(2, sheet.max_row + 1):
	VSL_NAME.append(sheet['B' + str(row)].value)
	VOY.append(sheet['C' + str(row)].value)
	TERMINAL.append(sheet['D' + str(row)].value)
	IGM_NO.append(sheet['E' + str(row)].value)
	IGM_DATE.append(sheet['F' + str(row)].value)
	ACCOUNT.append(sheet['G' + str(row)].value)
	CONTAINER_NO.append(sheet['H' + str(row)].value)
	SIZE.append(sheet['I' + str(row)].value)
	STATUS.append(sheet['J' + str(row)].value)
	ICD_LOCAL.append(sheet['K' + str(row)].value)
	POD.append(sheet['L' + str(row)].value)
	DISCHARGE_DATE.append(sheet['M' + str(row)].value)
	RAIL_ROUD_OUT.append(sheet['N' + str(row)].value)
	EMPTY_IN.append(sheet['O' + str(row)].value)
	YARD.append(sheet['P' + str(row)].value)

