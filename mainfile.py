#interactive python file with user inputs
input_file = input("Enter the name of the file to read and modify from: ").strip()
output_file = "output.txt"

try:
    #read the original content
    with open(input_file, 'r') as inputfile:
        essence = inputfile.read()
    # modify the original content and stores in a new file
    newEssence = essence.upper()
    with open(output_file, 'w') as outputfile:
        outputfile.write(newEssence)    
    print(f"Successfully modified '{input_file}' to '{output_file}'")
except FileNotFoundError:
    print("Ooops! File not found. Please check the filename again")    



#assessment: if a the file name isn't found an error is thrown
#          : if file is found, it is read, modified and a new file is created to display the modified content