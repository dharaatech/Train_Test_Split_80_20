import os
  
source = 'source/'
destination_80 = 'destination_80/'
# destination_20 = 'destination_20/'

# list of all files  
allfiles = os.listdir(source)
allfiles.sort()
print(allfiles)

# list of 80% files
list80 = allfiles[:int(len(allfiles)*0.8)]
list80.sort()
print(list80)

for f in list80:
    os.rename(source + f, destination_80 + f)





# # list_80 = ['1 - Copy (2).txt', '1 - Copy (3).txt', '1 - Copy (4).txt']
# # print(list_80)

# # list_20 = ['1 - Copy (5).txt', '1 - Copy.txt', '1.txt']
# # print(list_20)
  
# for f in list80:
#     os.rename(source + f, destination_80 + f)

# # for f in list_20:
# #     os.rename(source + f, destination_20 + f)






# # allfiles = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


