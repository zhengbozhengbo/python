import xlrd

def duqu():
    shuju = []
    f = xlrd.open_workbook(r'd:\ap框架\app框架\date\test数据.xlsx')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        shuju.append(sheet.row_values(i))
    return shuju

def duqu1():
    with open(r'd:\ap框架\app框架\date\run.txt','r') as f:
        shuju = f.readlines()
    return shuju

if __name__ == '__main__':
    print(duqu())
