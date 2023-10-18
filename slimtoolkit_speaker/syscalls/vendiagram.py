import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
# from matplotlib_venn import venn2, venn3
# from openpyxl import Workbook



def dict_to_excel(inputfile,outputfile):
    df = pd.DataFrame.from_dict(inputfile, orient='index').transpose()
    df.to_excel(outputfile, index=False)


def sort_dict_by_keys(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
    return sorted_dict



def excel_to_dict(file_name):
    df = pd.read_excel(file_name)
    categories = df['category'].unique()
    result_dict = {}
    for category in categories:
        system_calls = df[df['category'] == category]['Items'].tolist()
        result_dict[category] = system_calls

    return result_dict

def file_to_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines = list(set(lines))
    return lines



file_name = 'confine_allowed_httpd.txt'
allowed_confine_httpd = file_to_list(file_name)
file_name1 = 'speaker_allowed_httpd.txt'
allowed_speaker_httpd = file_to_list(file_name1)
file_name2 = 'slimtoolkit_allowed_httpd.txt'
allowed_slimtoolkit_httpd = file_to_list(file_name2)
file_name = 'categorization.xlsx'
data_dict = excel_to_dict(file_name)


print(len(allowed_speaker_httpd))

confine = {key: [value for value in values if value in allowed_confine_httpd] for key, values in data_dict.items()}
speaker = {key: [value for value in values if value in allowed_speaker_httpd] for key, values in data_dict.items()}
slimtoolkit = {key: [value for value in values if value in allowed_slimtoolkit_httpd] for key, values in data_dict.items()}
# print("confine:", confine)
# print("speaker:", speaker)
# print("slimtoolkit:",slimtoolkit)
dict_to_excel(confine,"/home/talha/Downloads/sproj/fw/syscalls/report/confine.xlsx")
dict_to_excel(speaker,"/home/talha/Downloads/sproj/fw/syscalls/report/speaker.xlsx")
dict_to_excel(slimtoolkit,"/home/talha/Downloads/sproj/fw/syscalls/report/slimtoolkit.xlsx")



common = {}
for key in confine.keys():
    common_values = set(confine[key]) & set(speaker[key]) & set(slimtoolkit[key])
    common[key] = list(common_values)

# print("Common:",common)
dict_to_excel(common,"/home/talha/Downloads/sproj/fw/syscalls/report/common.xlsx")


confine_only = {key: list(set(confine[key]) - set(speaker[key]) - set(slimtoolkit[key])) for key in confine}
speaker_only = {key: list(set(speaker[key]) - set(confine[key]) - set(slimtoolkit[key])) for key in speaker}
slimtoolkit_only = {key: list(set(slimtoolkit[key]) - set(confine[key]) - set(speaker[key])) for key in slimtoolkit}



# unique_elements = {}
# for key, value in speaker.items():
#     confine_value = confine.get(key, [])
#     slimtoolkit_value = slimtoolkit.get(key, [])
#     unique_elements[key] = list(set(value) - set(confine_value) - set(slimtoolkit_value))
# print(unique_elements)
# print("confine_only:",confine_only)
print("speaker_only:",speaker_only)
# print("slimtoolkit_only:",slimtoolkit_only)
dict_to_excel(confine_only,"/home/talha/Downloads/sproj/fw/syscalls/report/confine_only.xlsx")
dict_to_excel(speaker_only,"/home/talha/Downloads/sproj/fw/syscalls/report/speaker_only.xlsx")
dict_to_excel(slimtoolkit_only,"/home/talha/Downloads/sproj/fw/syscalls/report/slimtoolkit_only.xlsx")


confine_speaker_only = {key: list(set(confine[key]) & set(speaker[key]) - set(slimtoolkit[key])) for key in confine}
slimtoolkit_speaker_only = {key: list(set(slimtoolkit[key]) & set(speaker[key]) - set(confine[key])) for key in slimtoolkit}
confine_slimtoolkit_only = {key: list(set(confine[key]) & set(slimtoolkit[key]) - set(speaker[key])) for key in confine}

# print("confine_speaker_only:",confine_speaker_only)
# print("slimtoolkit_speaker_only:",slimtoolkit_speaker_only)
# print("confine_slimtoolkit_only:",confine_slimtoolkit_only)
dict_to_excel(confine_speaker_only,"/home/talha/Downloads/sproj/fw/syscalls/report/confine_speaker_only.xlsx")
dict_to_excel(slimtoolkit_speaker_only,"/home/talha/Downloads/sproj/fw/syscalls/report/slimtoolkit_speaker_only.xlsx")
dict_to_excel(confine_slimtoolkit_only,"/home/talha/Downloads/sproj/fw/syscalls/report/confine_slimtoolkit_only.xlsx")


# data_dict = sort_dict_by_keys(data_dict)
# common = sort_dict_by_keys(common)
# confine_only = sort_dict_by_keys(confine_only)
# speaker_only = sort_dict_by_keys(speaker_only)
# slimtoolkit_only = sort_dict_by_keys(slimtoolkit_only)
# confine_speaker_only = sort_dict_by_keys(confine_speaker_only)
# confine_slimtoolkit_only = sort_dict_by_keys(confine_slimtoolkit_only)
# slimtoolkit_speaker_only = sort_dict_by_keys(slimtoolkit_speaker_only)


# all_lengths = [len(data_dict[key]) for key in data_dict]
# common_lengths = [len(common[key]) for key in common]
# confine_only_lengths = [len(confine_only[key]) for key in confine_only]
# speaker_only_lengths = [len(speaker_only[key]) for key in speaker_only]
# slimtoolkit_only_lengths = [len(slimtoolkit_only[key]) for key in slimtoolkit_only]
# confine_speaker_lengths = [len(confine_speaker_only[key]) for key in confine_speaker_only]
# confine_slimtoolkit_lengths = [len(confine_slimtoolkit_only[key]) for key in confine_slimtoolkit_only]
# slimtoolkit_speaker_lengths = [len(slimtoolkit_speaker_only[key]) for key in slimtoolkit_speaker_only]



# plt.figure(figsize=(8, 8))
# venn3(subsets=(sum(confine_only_lengths), sum(speaker_only_lengths), sum(common_lengths), sum(slimtoolkit_only_lengths), 0, 0, 0),
#       set_labels=("Confine Only", "Speaker Only", "Slimtoolkit Only"))

# # Set the title
# plt.title("Venn Diagram")

# # Add the lengths as text on the diagram
# plt.text(-0.3, 0, str(sum(confine_only_lengths)), color='white', fontsize=12)
# plt.text(0.3, 0, str(sum(speaker_only_lengths)), color='white', fontsize=12)
# plt.text(0, 0.3, str(sum(common_lengths)), color='white', fontsize=12)
# plt.text(0, -0.3, str(sum(slimtoolkit_only_lengths)), color='white', fontsize=12)

# # Save the plot as a PNG file
# # plt.savefig('venn_diagram.png')


# # Save the plot as a PNG file
# plt.savefig('/home/talha/Downloads/sproj/fw/syscalls/report/venn_diagram.png')