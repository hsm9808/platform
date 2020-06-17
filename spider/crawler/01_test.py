import xlwt

workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('sheet1')  # 创建工作表


for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet.write(i, j, (i+1)*(j+1))
workbook.save('student.xls')
