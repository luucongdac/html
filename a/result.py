path = r' C:\temp\ATT_Temp\200901_1326_Sim_Pata_EnvironmentVariables_Dy_10_15              '


path = path.replace(' ','')
array_ = []
file = open(path + '\Rubasa\ATT_Report.xml',"r")
for i in file:
    i= i.replace('</TestCaseName><TestCaseVerdict>','\n')
    array_.append(i)

result = []
count = -1
for i in array_:
    a = i.split('<!')
    for j in a:
        #print(j)
        if '</TestCaseVerdict>' in j:
            count += 1
            result.append('')
        if '></Signal><Expected>' in j:
            j = j.replace(']]></Signal><Expected>','')
            j = j.replace('[CDATA[','')
            if result[count] == '':
                result[count] = result[count] + j
            else:
                result[count] = result[count]+ '\t'  + j
            #print(j)

#print(len(result))
for i in result:
    i = i.replace(' ','')
    print(i)
