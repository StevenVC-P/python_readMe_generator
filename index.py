# class questions:
#     def __init__(self, message):
#         self.message = message

# list = []

# list.append(questions('What is your user title?'))
# list.append(questions('Please describe your application'))
# list.append(questions('What are the steps to install?'))
# list.append(questions('What is your user title?'))
# list.append(questions('Please explain how to use the applicaiton'))
# list.append(questions('Mention your contributors here'))
# list.append(questions('What tests do you suggest?'))
# list.append(questions('What is your Github UserName?'))
# list.append(questions('What is your e-mail?'))

title = input("What is your project title?: ")
description = input("Please describe your application: ")
steps = input("What are the steps to install?: ")
use = input("Please explain how to use the applicaiton: ")
contributors = input("Mention your contributors here: ")
tests = input("What tests are suggested?: ")
github = input("What is your Github username?: ")
email = input("What is your e-mail?: ")

def selectFromDict(options, name):

    index = 0
    indexValidList = []
    print('Select a ' + name + ':')
    for optionName in options:
        index = index + 1
        indexValidList.extend([options[optionName]])
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ': ')
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            print('Selected ' + name + ': ' + selected)
            inputValid = True
            break
        else:
            print('Please select a valid ' + name + ' number')
    
    return selected

options = {}
options['Mozzila Public License 2.0'] = 'Mozzila Public License 2.0'
options['Appache 2.0 License'] = 'Appache 2.0 License'
options['The MIT License'] = 'The MIT License'
options['Boost Software License 1.0'] = 'Boost Software License 1.0'
options['The Unlicense'] = 'The Unlicense'

# Let user select a month
option = selectFromDict(options, 'License')

