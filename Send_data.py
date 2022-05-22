import datetime
import paramiko
import os, glob, sys
import time

#vsharma@volta.sdsu.edu ktveEBUC


#=================================================================================================================================================================

day_time = datetime.datetime.now()
#print(day_time)

#=================================================================================================================================================================

MLR_op = []

with open("MultiLR.txt","r") as f:
    MLR_op = f.read().splitlines()

M_power = MLR_op[0]
MLR_power = float(M_power)


#print(M_power)
#MLR_price = MLR_op[1]
#print(MLR_price)
    
#=================================================================================================================================================================

# Threshold value for each hour. 
# Each hourly threshold value is the average power consumption value for that particular hour.
# This average power consumption value is specific to the dataset/hour.

th1 = 82.73/365
th2 = 66.885/365
th3 = 61.57/365
th4 = 58.05/365
th5 = 57.595/365
th6 = 64.97/365
th7 = 82.525/365
th8 = 102.32/365
th9 = 136.195/365
th10 = 172.52/365
th11 = 201.91/365
th12 = 209.495/365
th13 = 208.405/365
th14 = 210.77/365
th15 = 196.365/365
th16 = 217.675/365
th17 = 228.44/365
th18 = 220.765/365
th19 = 254.735/365
th20 = 287.98/365
th21 = 238.94/365
th22 = 188.94/365
th23 = 142.58/365
th24 = 109.635/365

th_lst = [th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, th11, th12, th13, th14, th15, th16, th17, th18, th19, th20, th21, th22, th23, th24]


hour = datetime.datetime.now().hour
#print(hour)
 
#=================================================================================================================================================================




#=================================================================================================================================================================


current_th = th_lst[hour]

if(current_th < MLR_power): # Overconsumption send 1; PC values will be +ve
    Final_string = "Date and Time:"+str(day_time) +"\t"+ "PC:"+str(MLR_power) +"\t"+ "Difference:"+str(MLR_power - current_th) +"\t\t"+ "WarningLevel: 1"


else: # within bound send 0; PC values will be -ve
    Final_string = "Date and Time:"+str(day_time) +"\t"+ "PC:"+str(MLR_power) +"\t"+ "Difference:"+str(MLR_power - current_th) +"\t\t"+ "WarningLevel: 0"
    
#print(Final_string)


ssh_str = f"echo {Final_string}>>MLR/Blackout_Data_Log.txt"


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='volta.sdsu.edu',port='22',username='vsharma',password='ktveEBUC',look_for_keys=False, allow_agent=False)

stdin,stdout,stderr=ssh_client.exec_command(ssh_str)
time.sleep(1)  #Add delay to avoid error
#stdin,stdout,stderr=ssh_client.exec_command("cat MLR/abc.txt")
#print(stdout.read().decode())
ssh_client.close()

#=================================================================================================================================================================


