import json

'''
This code file will read the coefficient text file and will generate a JSON file.
The JSON file will contain the intercept and coefficients values of all 24 csv files.
The intercept and coefficient values are stored in the form of list of lists.
'''


f = open("D:\\Thesis\Done___code\\MLR\\MLR_final_final_20th_aug\\after sending\\no C_ MLR_final\MLR_final\\coefficients_auto.txt","r")


#----------------------------------------------------------)
# for 1
a1 = f.readline()
a1 = a1.replace('\t', ",")
a1 = a1.rstrip()
a1 = a1.rstrip(",")
a1 = list(a1.split(","))
a1 = list(map(float, a1))
ls1 = a1
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 2
a2 = f.readline()
a2 = a2.replace('\t', ",")
a2 = a2.rstrip()
a2 = a2.rstrip(",")
a2 = list(a2.split(","))
a2 = list(map(float, a2))
ls2 = a2
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 3
a3 = f.readline()
a3 = a3.replace('\t', ",")
a3 = a3.rstrip()
a3 = a3.rstrip(",")
a3 = list(a3.split(","))
a3 = list(map(float, a3))
ls3 = a3
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 4
a4 = f.readline()
a4 = a4.replace('\t', ",")
a4 = a4.rstrip()
a4 = a4.rstrip(",")
a4 = list(a4.split(","))
a4 = list(map(float, a4))
ls4 = a4
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 5
a5 = f.readline()
a5 = a5.replace('\t', ",")
a5 = a5.rstrip()
a5 = a5.rstrip(",")
a5 = list(a5.split(","))
a5 = list(map(float, a5))
ls5 = a5
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 6
a6 = f.readline()
a6 = a6.replace('\t', ",")
a6 = a6.rstrip()
a6 = a6.rstrip(",")
a6 = list(a6.split(","))
a6 = list(map(float, a6))
ls6 = a6
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 7
a7 = f.readline()
a7 = a7.replace('\t', ",")
a7 = a7.rstrip()
a7 = a7.rstrip(",")
a7 = list(a7.split(","))
a7 = list(map(float, a7))
ls7 = a7
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 8
a8 = f.readline()
a8 = a8.replace('\t', ",")
a8 = a8.rstrip()
a8 = a8.rstrip(",")
a8 = list(a8.split(","))
a8 = list(map(float, a8))
ls8 = a8
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 9
a9 = f.readline()
a9 = a9.replace('\t', ",")
a9 = a9.rstrip()
a9 = a9.rstrip(",")
a9 = list(a9.split(","))
a9 = list(map(float, a9))
ls9 = a9
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 10
a10 = f.readline()
a10 = a10.replace('\t', ",")
a10 = a10.rstrip()
a10 = a10.rstrip(",")
a10 = list(a10.split(","))
a10 = list(map(float, a10))
ls10 = a10
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 11
a11 = f.readline()
a11 = a11.replace('\t', ",")
a11 = a11.rstrip()
a11 = a11.rstrip(",")
a11 = list(a11.split(","))
a11 = list(map(float, a11))
ls11 = a11
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 12
a12 = f.readline()
a12 = a12.replace('\t', ",")
a12 = a12.rstrip()
a12 = a12.rstrip(",")
a12 = list(a12.split(","))
a12 = list(map(float, a12))
ls12 = a12
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 13
a13 = f.readline()
a13 = a13.replace('\t', ",")
a13 = a13.rstrip()
a13 = a13.rstrip(",")
a13 = list(a13.split(","))
a13 = list(map(float, a13))
ls13 = a13
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 14
a14 = f.readline()
a14 = a14.replace('\t', ",")
a14 = a14.rstrip()
a14 = a14.rstrip(",")
a14 = list(a14.split(","))
a14 = list(map(float, a14))
ls14 = a14
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 15
a15 = f.readline()
a15 = a15.replace('\t', ",")
a15 = a15.rstrip()
a15 = a15.rstrip(",")
a15 = list(a15.split(","))
a15 = list(map(float, a15))
ls15 = a15
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 16
a16 = f.readline()
a16 = a16.replace('\t', ",")
a16 = a16.rstrip()
a16 = a16.rstrip(",")
a16 = list(a16.split(","))
a16 = list(map(float, a16))
ls16 = a16
#----------------------------------------------------------)




#----------------------------------------------------------)
# for 17
a17 = f.readline()
a17 = a17.replace('\t', ",")
a17 = a17.rstrip()
a17 = a17.rstrip(",")
a17 = list(a17.split(","))
a17 = list(map(float, a17))
ls17 = a17
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 18
a18 = f.readline()
a18 = a18.replace('\t', ",")
a18 = a18.rstrip()
a18 = a18.rstrip(",")
a18 = list(a18.split(","))
a18 = list(map(float, a18))
ls18 = a18
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 19
a19 = f.readline()
a19 = a19.replace('\t', ",")
a19 = a19.rstrip()
a19 = a19.rstrip(",")
a19 = list(a19.split(","))
a19 = list(map(float, a19))
ls19 = a19
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 20
a20 = f.readline()
a20 = a20.replace('\t', ",")
a20 = a20.rstrip()
a20 = a20.rstrip(",")
a20 = list(a20.split(","))
a20 = list(map(float, a20))
ls20 = a20
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 21
a21 = f.readline()
a21 = a21.replace('\t', ",")
a21 = a21.rstrip()
a21 = a21.rstrip(",")
a21 = list(a21.split(","))
a21 = list(map(float, a21))
ls21 = a21
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 22
a22 = f.readline()
a22 = a22.replace('\t', ",")
a22 = a22.rstrip()
a22 = a22.rstrip(",")
a22 = list(a22.split(","))
a22 = list(map(float, a22))
ls22 = a22
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 23
a23 = f.readline()
a23 = a23.replace('\t', ",")
a23 = a23.rstrip()
a23 = a23.rstrip(",")
a23 = list(a23.split(","))
a23 = list(map(float, a23))
ls23 = a23
#----------------------------------------------------------)



#----------------------------------------------------------)
# for 24
a24 = f.readline()
a24 = a24.replace('\t', ",")
a24 = a24.rstrip()
a24 = a24.rstrip(",")
a24 = list(a24.split(","))
a24 = list(map(float, a24))
ls24 = a24
#----------------------------------------------------------)


f.close()



final = [ls1,ls2,ls3,ls4,ls5,ls6,ls7,ls8,ls9,ls10,ls11,ls12,ls13,ls14,ls15,ls16,ls17,ls18,ls19,ls20,ls21,ls22,ls23,ls24]
#print(final)




f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\header_coefficients.json","w")

json.dump(final,f)

f.close()







