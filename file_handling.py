try :
    with open(input("Enter file name:"), 'r') as file:
        content = file.read()
    modified_content = content.upper()   # to change to uppercase
    with open(input("Enter output file name:"), 'w') as output_file:
        output_file.write(modified_content)
 
except FileNotFoundError: 
    print('File not found or could not be opened.')
    
except Exception as e:
    print(f'An error occurred: {e}')