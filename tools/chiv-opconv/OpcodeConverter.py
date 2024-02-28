import shutil as sh

# Opcode converter but with escaper

# init the path subsystem

print("Opcode Converter v1 by Harraf")
print("---")
isfile = str(input("Please input a file to convert: "))
prompt = str(input("Do you want to use a template? (type 'y' if yes, type anything else for no) ")).lower()
tUse = False
tsFile = ""
if prompt == "y":
    tUse = True
    tsFile = str(input("Input a file to use as a template: "))
print("---")
ifile = open(isfile, "r")
idata = ifile.read()
ifile.close()
print("Convering Data...")
stage1 = idata.split("\n")
# Escape some forms of chars
stageE = []
for i in range(len(stage1)):
    stageE.append(stage1[i].replace("\\n", "\n").replace("\"", "\\\"").replace("\\", "\\\\").replace("\n", "\\n"))
odata = "["
for i in range(len(stageE)):
    odata += "\"" + str(stageE[i]) + "\", "
odata = odata[0 : len(odata) - 2] + "]"
print("Conversion Complete!")
if tUse == True:
    tfile = open(tsFile, "r")
    tdata = tfile.read()
    tfile.close()
    print("Putting Data into template...")
    odata = tdata.replace("$t", odata)
    print("Done!")
    
print("Data:")
print(odata)
