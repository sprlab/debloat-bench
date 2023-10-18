import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pickle
import PyPDF2
from PIL import Image
import matplotlib.backends.backend_pdf as pdf_backend
import os
import glob


def create_bar_chart(data, output_file,y_lab):
    # Extract the applications and their values
    applications = set()
    values = {}

    for entry in data:
        for key, app_list in entry.items():
            for app_dict in app_list:
                for app, value in app_dict.items():
                    applications.add(app)
                    if key not in values:
                        values[key] = {}
                    values[key][app] = value

    # Prepare data for plotting
    x = np.arange(len(applications))
    width = 0.2
    fig, ax = plt.subplots()
    offset = -width * (len(data) // 2)

    for i, entry in enumerate(data):
        key = list(entry.keys())[0]
        y = [values[key].get(app, 0) for app in applications]
        ax.bar(x + offset, y, width=width, label=key)
        offset += width

    # Set the x-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(applications)

    # Set the y-axis label
    ax.set_xlabel('Applications')
    ax.set_ylabel(y_lab)

    # Set the legend
    ax.legend()

    # Save the plot as a PNG file
    plt.savefig(output_file)



def extract_values_from_files(directory,stringz):
    # Get all the files in the specified directory
    files = os.listdir(directory)
    # Filter files that have "test" in their names
    filtered_files = [filename for filename in files if stringz in filename]
    # Create a dictionary to store the values
    result = {}
    for filename in filtered_files:
        # Split the filename into components
        components = filename.split('_')
        # Extract the key and subkey
        key = components[0]
        subkey = os.path.splitext(components[2])[0]  # Remove the extension
        # Read the value from the file
        with open(os.path.join(directory, filename), 'r') as file:
            value = int(file.read())
        # Add the value to the result dictionary
        if key not in result:
            result[key] = []
        result[key].append({subkey: value})
    # Convert the dictionary into the desired list format
    final_result = []
    for key, values in result.items():
        final_result.append({key: values})
    return final_result


def extract_sizes_from_files(directory):
    # Get all the files in the specified directory
    files = os.listdir(directory)

    # Filter files that have "size" in their names
    filtered_files = [filename for filename in files if 'size' in filename]

    # Initialize dictionaries to store the sizes
    original_size = {}
    debloated_size = {}

    for filename in filtered_files:
        # Extract the application name from the file name
        app_name = filename.split('_')[2].split('.')[0]

        # Read the floating-point numbers from the file
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()

        # Extract the sizes from the lines
        if len(lines) >= 2:
            original = float(lines[0].strip())
            debloated = float(lines[1].strip())
            original_size[app_name] = original
            debloated_size[app_name] = debloated

    return original_size, debloated_size

def create_bar_chart2(original_size, debloated_size, output_file):
    applications = list(original_size.keys())
    x = np.arange(len(applications))
    width = 0.35

    original_values = list(original_size.values())
    debloated_values = list(debloated_size.values())

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, original_values, width, label='Original Size')
    rects2 = ax.bar(x + width/2, debloated_values, width, label='Debloated Size')

    ax.set_xlabel('Applications')
    ax.set_ylabel('Size Reduction')
    ax.set_xticks(x)
    ax.set_xticklabels(applications)
    ax.legend()

    plt.savefig(output_file)


def count_system_calls(directory):
    # Get all the files in the specified directory
    files = os.listdir(directory)
    # Filter files that have "test" in their names
    filtered_files = [filename for filename in files if 'allowed' in filename]
    # Create a dictionary to store the values
    result = {}
    print(filtered_files)
    for filename in filtered_files:
        # Split the filename into components
        components = filename.split('_')
        # Extract the key and subkey
        key = components[0]
        subkey = os.path.splitext(components[2])[0]  # Remove the extension
        # Read the value from the file
        with open(os.path.join(directory, filename), 'r') as file:
            # value = int(22)
            lines = file.readlines()
            value = 326 - len(lines)
        # Add the value to the result dictionary
        if key not in result:
            result[key] = []
        result[key].append({subkey: value})
    # Convert the dictionary into the desired list format
    final_result = []
    for key, values in result.items():
        final_result.append({key: values})
    return final_result


def create_pdf_from_pngs(output_file):
    png_files = glob.glob('*.png')
    png_files = sorted(png_files)
    # Print the list of PNG files
    print(png_files)
    pdf_pages = pdf_backend.PdfPages(output_file)
    dpi = 350

    for i in range(len(png_files)):
        fig1 = plt.figure()
        plt.imshow(plt.imread(png_files[i]))
        plt.axis('off')
        pdf_pages.savefig(fig1, dpi=dpi, bbox_inches='tight', pad_inches=0)
        plt.close(fig1)    
    # Close the PDF file
    pdf_pages.close()



#  CORRECTNESS
directory = './results'
data = extract_values_from_files(directory,'test')
print(data)
output_file = './results/Correctness.png'
create_bar_chart(data, output_file, 'Correct test cases')

#  CVES
#data = extract_values_from_files(directory,'CVE')
#print(data)
#output_file = 'cve.png'
#create_bar_chart(data, output_file, 'CVEs mitegated')

# SIZES
original_size, debloated_size = extract_sizes_from_files(directory)
print("Original Size:", original_size)
print("Debloated Size:", debloated_size)
create_bar_chart2(original_size,debloated_size,'./results/Size.png')

# SYS CALLS
data = count_system_calls(directory)
print(data)
output_file = './results/syscall.png'
create_bar_chart(data, output_file, 'system calls reduced')

# REPORT
output_file = './results/report.pdf'
create_pdf_from_pngs(output_file)
