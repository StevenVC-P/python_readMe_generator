title = input("What is your project title?: ")
description = input("Please describe your application: ")
steps = input("What are the steps to install?: ")
usage = input("Please explain how to use the applicaiton: ")
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
            return selected
        else:
            print('Please select a valid ' + name + ' number')    

options = {}
options['Mozzila Public License 2.0'] = 'Mozzila Public License 2.0'
options['Appache 2.0 License'] = 'Appache 2.0 License'
options['The MIT License'] = 'The MIT License'
options['Boost Software License 1.0'] = 'Boost Software License 1.0'
options['The Unlicense'] = 'The Unlicense'

# Let user select an option
option = selectFromDict(options, 'License')

def licenseInfo():
    if option == 'Mozzila Public License 2.0':
        badge = '[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)]'
        licenseURL = 'https://opensource.org/licenses/MPL-2.0'
    
    if option == 'Appache 2.0 License':
        badge = '[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)]'
        licenseURL = 'https://opensource.org/licenses/Apache-2.0'

    if option == 'The MIT License':
        badge = '[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]'
        licenseURL = 'https://opensource.org/licenses/MIT'

    if option == 'Boost Software License 1.0':
        badge = '[![License](https://img.shields.io/badge/License-Boost%201.0-lightblue.svg)]'
        licenseURL = 'https://www.boost.org/LICENSE_1_0.txt'

    if option == 'The Unlicense':
        badge = '[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)]'
        licenseURL = 'http://unlicense.org/'
    return (badge, licenseURL)

badge = licenseInfo()

def markDown():
    f = open("readMe.md", "r+")
    f.truncate(0)
    f.write(
f'''# {title}

{badge}

## Description
{description}

##  Table of Contents

* [Installation](#Installation)
* [Usage](#Usage)
* [License](#License)
* [Contributing](#Contributing)
* [Tests](#Tests)
* [Questions](#Questions)

## Installation
{steps}

## Usage
{usage}

## License
{option}
Please review [data.licenseURL](data.licenseURL) to understand the license.

## Contributing
{contributors}

## Tests
{tests}

## Questions
Come checkout my Github!

{github}(https://www.github/{github})

And if you have any questions you can e-mail me at:
[{email}]({email})

''')
    f.close()

markDown()
