import xlsxwriter
import datetime

# Create a workbook and add a worksheet

workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.



worksheet.write(0, 0, 'Sr. No.')
worksheet.write(0, 1, 'VSL NAME')
worksheet.write(0, 2, 'VOY')
worksheet.write(0, 3, 'TERMINAL')
worksheet.write(0, 4, 'IGM DATE')
worksheet.write(0, 5, 'ACCOUNT')
worksheet.write(0, 6, 'CONTAINER NO')
worksheet.write(0, 7, 'SIZE')
worksheet.write(0, 8, 'STATUS')
worksheet.write(0, 9, 'ICD/LOCAL')
worksheet.write(0, 10, 'POD')
worksheet.write(0, 11, 'DISCHARGE DATE')
worksheet.write(0, 12, 'RAIL/ROAD OUT')
worksheet.write(0, 13, 'EMPTY IN')
worksheet.write(0, 14, 'YARD')
worksheet.write(0, 15, 'REMARKS')

row=1
col=0

for container in containerToWrite
	worksheet.write(row,col,row)
	worksheet.write(row,col,container.VSL_NAME)
	worksheet.write(row,col,container.VOY)
	worksheet.write(row,col,container.TERMINAL)
	worksheet.write(row,col,container.IGM_DATE)
	worksheet.write(row,col,container.ACCOUNT)
	worksheet.write(row,col,container.CONTAINER_NO)
	worksheet.write(row,col,container.SIZE)
	worksheet.write(row,col,container.STATUS)
	worksheet.write(row,col,container.ICD/LOCAL)
	worksheet.write(row,col,container.POD)
	worksheet.write(row,col,container.DISCHARGE_DATE)
	worksheet.write(row,col,container.RAIL/ROAD_OUT)
	worksheet.write(row,col,container.EMPTY_IN)
	worksheet.write(row,col,container.YARD)
	worksheet.write(row,col,container.REMARKS)
	row=row+1
	col=col+1

workbook.close()
