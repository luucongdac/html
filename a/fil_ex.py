

path = ' C:/01_ASW/TOY_PF19_CMP_BL17_Integration_3/ToyotaCMP_BB97973/_Test/UT_063_SnapshotRecordFunctions_TOYOTA_BB97973/Cantata/tests/atest_SnapshotRecordFunctions_TOYOTA/atest_SnapshotRecordFunctions_TOYOTA.ctr '


path = path.replace(' ','')
t_ = path
path_c = path.replace('.ctr','.c')

w = open('C:/Users/LUD5HC.APAC.000.001/Desktop/b.txt','w')

o = open(path).readlines()

class testcase_false:
    def __init__(self,name):
        self.name_testcase = name
        self.temp = []
        self.false_testcase = []
        self.result = []
    def print_all(self):
        print(self.name_testcase)
        for i in self.result:
            print(i)
        print('-----------'*10)
total_wrong = []
flag = False
count = 0
buffer = []
#collect ctr
for i in o:
    if '------------------------- Start Test: ' in i:
        t = i.split(': ')
        t1 = t[1] +': ' + t[2]
        total_wrong.append(testcase_false(t1))
        flag = True
    if '------------------------- End Test: ' in i:
        flag = False
        total_wrong[count].temp = buffer
        count += 1
        buffer = []
    if flag == True:
        buffer.append(i)
        
     
#analyze ctr
for obj in total_wrong:
    #obj.print_all()
    temp = ''
    flag = False
    for i in obj.temp:
        if '>>  FAILED: Check: ' in i and not '>>  FAILED: Check Memory:' in i:
            flag = True
        if 'expected:' in i and not 'U.' in i and not '.U' in i and not 'UU' in i:
            flag = False
            temp = temp + i
            obj.false_testcase.append(temp)
            temp = ''
        if flag == True:
            temp = temp + i
anpha = ['A','B','C','D','E','F']
for obj in total_wrong:
    temp = []
    name = ''
    value = ''
    #print(obj.name_testcase)
    for i in obj.false_testcase:
        #print('raw',i)
        t = i.split('=')
        #print('split',t)
        t5 = t[1]
        #print(t5)
        t6 = t5.split('actual:')
        name = t6[0]
        name = name.replace('\n','')
        #print('name',name)
        t1 = t[1]
        #print(t1)
        t2 = t1.split('actual: ')
        t7 = t2[1].split('expected: ')
        t3 = t7[0]
        t4 = t3.split(' ')
        value = t4[0]
        value = value.replace('\n','')
        if value == 'True':
            value = 'true'
        if value == 'False':
            value = 'false'
        for t_ in anpha:
            if t_ in value and not '0x' in value:
                value =  '0x' + value
        value = value + ';'
        #print(value)
        temp.append(name + ' = ' + value)
    obj.result = temp
        
for obj in total_wrong:
    obj.print_all() 
    
#write expected 
o = open(path_c).readlines()

for i in o:
    if('START_TEST(' in i):
        t = i
        t1 = t.split('(')
        t2 = t1[1].replace('"','')
        name_case = t2.replace(',','')
        for obj in total_wrong:
            if name_case == obj.name_testcase:
                for j in obj.result:
                    w.writelines('\t' + j + '\n')
    w.writelines(i)
w.close()
