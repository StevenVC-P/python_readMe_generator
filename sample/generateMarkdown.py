def markDown():

    f = open("readMe.md", "r+")
    f.truncate(0)
    f.write(
f'''# data.title

data.badge

## Description
data.description

##  Table of Contents

* [Installation](#Installation)
* [Usage](#Usage)
* [License](#License)
* [Contributing](#Contributing)
* [Tests](#Tests)
* [Questions](#Questions)

## Installation
data.installation

## Usage
data.usage

## License
data.license
Please review [data.licenseURL](data.licenseURL) to understand the license.

## Contributing
data.contributing

## Tests
data.tests

## Questions
Come checkout my Github!

[data.github](https://www.github/data.github)

And if you have any questions you can e-mail me at:
[data.email](data.email)

''')
    f.close()

markDown()