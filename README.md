# docker<br>
**Download Vagrant and virtual box using:**<br>
```sudo apt-get install -y vagrant```<br>
```sudo apt-get install -y virtualbox```
<br>
**Now start the Virtual machine using:**<br>
```vagrant up```
<br>
**Once the VM starts, connect to it using:**<br>
```vagrant ssh```
<br>
**Go inside the folder named vagrant_data:**<br>
```cd vagrant_data```
<br>
**Now you can run the becnhmark using main.py file. Check the help functionality using:**<br>
```python3 orchestrator.py -h```<br>
**All the tools can be run using:**<br>
```python3 orchestrator.py -t all```<br>
**Specific tools can be run using:**<br>
```python3 orchestrator.py -t toolname```<br>
**This will generate all the data inside data folder. To generate the reports go inside the data folder. Get the report using:** <br>
```python3 measurement.py```<br>
**To get the syscalls category report go inside the Allowed_data folder and type:** <br>
```python3 final.py```<br>
To add more applications, go => configurations => you_tool => create new json file to add new applications just like others. Also add the corresponding test cases in TestCases directory. <br>
To add more tools create tool.py similar to slimtoolkit.py and speaker.py <br>
Remember to add the configurations of newly added tool. <br>
Next step: for adding new tool, I'll create a base class with all the common functionalities like including running test cases, running train cases for dynamic tools etc. so that adding new tools will get easier.
