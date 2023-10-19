# Debloat Bench C

## Setup Instructions

**Install Vagrant and VirtualBox**

To set up the framework, you'll need to install Vagrant and VirtualBox. Use the following commands to install them on your system:

```
sudo apt-get install -y vagrant
sudo apt-get install -y virtualbox
```

## Running Tools

**Steps for running Confine** <br>

```cd confine``` <br>

**Start the Virtual machine using and connect to it using:** <br>
```
vagrant up
vagrant ssh
```

**Go inside the folder named vagrant_data:** <br>
```cd vagrant_data``` <br>

**Now you can run the becnhmark on confine using the run.py file.** <br>
This will debloat the container images and run the test cases and generate the relevant files.

**Steps for running Slimtoolkit and/or Speaker** <br>
```cd slimtoolkit_speaker``` <br>

**Start the Virtual machine using and connect to it using:** <br>
```
vagrant up
vagrant ssh
```

**Go inside the folder named vagrant_data:** <br>
```cd vagrant_data``` <br>

**Now you can run the becnhmark using main.py file. Check the help functionality using:** <br>
```python3 orchestrator.py -h``` <br>

**All the tools (currently Slimtoolkit and Speaker) can be run using:** <br>
```python3 orchestrator.py -t all``` <br>

**Specific tools can be run using:** <br>
```python3 orchestrator.py -t toolname``` <br>

This will generate all the data inside data folder. 

**To generate the reports go back to the main directory** <br>
```cd /path-to-debloath-bench``` <br>

**Generate the graphs for correctnes and system call reduction:**
```
python3 move.p
python3 measurement.py
```

## Extending the Framework

### Adding More Applications

To add more applications to the framework, follow these steps:

1. Navigate to the `configurations` directory.
2. Create a new JSON file to define the configurations for the new applications. Model it after the existing JSON files, ensuring you include all necessary details.
3. Additionally, add corresponding test cases for the new applications in the `TestCases` directory.

### Adding More Tools

To include new debloating tools, follow these steps:

1. Create a new Python file, e.g., `your_tool.py`, similar to the existing tool files such as `slimtoolkit.py` and `speaker.py`.
2. Remember to add the configurations and specifications for the newly added tool in the `configurations` directory.

We encourage contributions and the expansion of the framework to accommodate a broader range of applications and debloating tools.

Feel free to extend the framework's capabilities and make it more versatile!


## To-Do

Debloat Bench C has the following planned improvements:

1. **Integrate CVEs and their corresponding reports.**
   - This will enhance security assessment by including information on known vulnerabilities and their impacts.

2. **Automate the graph generation process.**
   - Automating graph generation will streamline data visualization and analysis.

3. **Add a feature to run all tools from a single file.**
   - Simplify the execution of debloating tools by providing a one-click option for running all available tools.

4. **Create a base class with common functionalities.**
   - Developing a base class with shared functionalities will simplify the addition of new debloating tools. It can include features like running test cases and training cases for dynamic tools.


**Feel free to contribute and help us make this framework even better!**




