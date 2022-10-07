# Project Modules

The repository contains global modules that are called by other projects in this GitHub account.
Modules like calling , populating or closing a json , excel or pdf file.
These modules may use external modules as well but they have specified towards
this specific use case and generally for Quantitative Analysis.

## Why?

The reason for separating these modules is they increasing get complex and 
no one want to keep copying a pasting functions or writing a new function 
altogether hence the need to separate and generalize/standardize them.

## Installation

-Clone the modules folder to your local machine 

-Call them in the code as you would call any other module or use
the sys.path.append method

```bash
  
path = "/Users/adamszequi/SmartFactor/Smart-Factor-Research-Files-5/Universal Models"
sys.path.append(path)
from ExternalModules import modulesSmartFactor

```
## Usage

'Open+" "' refers to modules that open files 
'Close+" "' refers to modules that close files 
