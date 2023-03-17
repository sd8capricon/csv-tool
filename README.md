# CSV-Tool

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. Once you have finished with me, you can create new files by opening the **file explorer** on the left corner of the navigation bar.


# How to run the tool

## Setup
`git clone https://github.com/sd8capricon/csv-tool.git`
`cd csv-tool`
`pip install -r requirements.txt`

## Run


### Use Tool Help
`python csvTool.py -h`
##### Supported Commands by the Tool
 - count (count number of rows)
- mean (mean of the given column)
- filter (filters the given column w.r.t given filter)
- std (standard deviation of the given column )
- sort
- exit
##### Flags
 -c specify command to work with
 -col specify column
 -f specify how to filter
 
Note: 
- after running the tool -c flag is not required to specify command
- -f flag only works with filter command, it wont have any effect on other commands


### With Only CSV File
Easiest way to get started is to to run the csvTool.py with your required csv file. Commands can also be provided when the tool is running
`python csvTool.py [pathToCsvFile]`
example
![eg img](imgs/without%20commands.png)

### Run With Optional Commands

`python csvTool.py [pathToCSVFile ] -c [command] -col [columnName] -f[filterHere]`
example
![eg img](imgs/Inkedwith%20commands.jpg)


# Optional Pandas

## Setup
same as standard tool

## Run
Run csvToolPandas.py instead of csvTool.py rest is similar to the standard tool