from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ContainerIn.models import *
from ContainerIn.forms import *
import openpyxl
# Create your views here.

@login_required
def Form(request):
    fileform = DocumentForm()
    if request.method=='POST':

        form = request.POST
        if form['VSL_NAME'] and form['VOY_NUMBER'] and form['CONTAINER_NO']:
            contain = ContainerIn()
            contain.VSL_NAME = form['VSL_NAME']
            contain.VOY_NUMBER = form['VOY_NUMBER']
            contain.TERMINAL = form['TERMINAL']
            contain.IGM_NO = form['IGM_NO']
            contain.IGM_DATE = form['IGM_DATE']
            contain.ACCOUNT = form['ACCOUNT']
            contain.CONTAINER_NO = form['CONTAINER_NO']
            contain.SIZE = form['SIZE']
            contain.STATUS = form['STATUS']
            contain.ICD_LOCAL = form['ICD_LOCAL']
            contain.POD = form['POD']
            contain.DISCHARGE_DATE = form['DISCHARGE_DATE']
            contain.RAIL_ROUND_OUT = form['RAIL_ROUD_OUT']
            contain.EMPTY_IN = form['EMPTY_IN']
            contain.YARD = form['YARD']
            contain.save()

        filein = DocumentForm(request.POST, request.FILES)
        if filein.is_valid():
            newfile = Documents()
            newfile.excel = filein.cleaned_data['docfile']
            newfile.save()


            wb = openpyxl.load_workbook(newfile.excel.path)
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

            for i in xrange(0, len(CONTAINER_NO)):
                container = ContainerIn()
                container.VSL_NAME = VSL_NAME[i]
                container.VOY_NUMBER = VOY[i]
                container.TERMINAL = TERMINAL[i]
                container.IGM_NO = IGM_NO[i]
                container.IGM_DATE = IGM_DATE[i]
                container.ACCOUNT = ACCOUNT[i]
                container.CONTAINER_NO = CONTAINER_NO[i]
                container.SIZE = SIZE[i]
                container.STATUS = STATUS[i]
                container.ICD_LOCAL = ICD_LOCAL[i]
                container.POD = POD[i]
                container.DISCHARGE_DATE = DISCHARGE_DATE[i]
                container.RAIL_ROUND_OUT = RAIL_ROUD_OUT[i]
                container.EMPTY_IN = EMPTY_IN[i]
                container.YARD = YARD[i]
                container.save()

        return render(request, "first.html")

    return render(request, 'Forms.html', {'fileform':fileform})
