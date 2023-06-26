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
