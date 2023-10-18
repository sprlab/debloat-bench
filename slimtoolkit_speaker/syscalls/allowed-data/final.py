import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import math


# Font sizes:

fontsize_labels = 14
fontsize_ticks = 12
fontsize_title = 16
bottom_adjustment = 0.2
save_images = '.pdf'
font_weight = 'normal'     # Use bold of you want


# All Applications
tools = ['speaker_','confine_','slimtoolkit_']
applications = ['mysql','httpd', 'nginx', 'node','redis','mongo','python']
case_study = ['redis', 'httpd', 'python']
#  Categorization
categorization = {"database":['mysql','redis','mongo'],"network":['httpd', 'nginx'], "language":['node','python']}


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


file_name = 'categorization.xlsx'
complete_data = excel_to_dict(file_name)
orginal_dict = {}
for key, value in complete_data.items():
    orginal_dict[key] = len(value)
orginal_dicts = dict(sorted(orginal_dict.items()))
orginal_dict = orginal_dicts
# print(orginal_dict)


# Creating 3 graphs for results section
for key,value in categorization.items():
    app = []
    for j in categorization[key]:
        for k in tools:
            file_name = k+j+'.txt'
            # print(file_name)
            allowed = file_to_list(file_name)
            filtered_dict = {key: [value for value in values if value in allowed] for key, values in complete_data.items()}
            filtered_dicts = dict(sorted(filtered_dict.items()))
            filtered_dict = filtered_dicts

            debloated_dict = {}
            for key1, value1 in filtered_dict.items():
                debloated_dict[key1] = len(value1)
            debloated_dicts = dict(sorted(debloated_dict.items()))
            debloated_dict = debloated_dicts
            app.append(debloated_dict)
        # print("app: ",app)
        last_dict_index = 0
    for i in range(3, len(app)):
        app[last_dict_index] = {key: app[last_dict_index].get(key, 0) + app[i].get(key, 0) for key in app[last_dict_index]}
        last_dict_index = (last_dict_index + 1) % 3
    app = app[0:3]
    # print("yup: ",len(categorization[key]))
    for dictionary in app:
        for key2 in dictionary:
            dictionary[key2] /= len(categorization[key])
            dictionary[key2] = math.ceil(dictionary[key2])
    # print(app)

    categories = list(orginal_dict.keys())
    v1 = list(orginal_dict.values())
    values = [list(d.values()) for d in app]
    # print(values)
    # print(v1)
    percentage_reduction = []

    for ii in range(len(values)):
        reduction = [((v1[jj] - values[ii][jj]) / v1[jj] * 100) for jj in range(len(v1))]
        percentage_reduction.append(reduction)
    # print(percentage_reduction)
    values = percentage_reduction
    # print(values)

    plt.figure(figsize=(10, 6))
    x = range(len(categories))
    bar_width = 0.2
    for ii, vals in enumerate(values):
        plt.bar(x=np.arange(len(categories)) + ii * bar_width, height=vals, width=bar_width, label=tools[ii])

    plt.xlabel('Systemcall Categories',fontsize = fontsize_labels, fontweight=font_weight)
    plt.ylabel('Percentage Syscalls Reduced',fontsize = fontsize_labels, fontweight=font_weight)
    plt.title('Comparison of syscalls allowed for '+key, fontsize = fontsize_title, fontweight=font_weight)
    plt.xticks(x, categories, fontsize = fontsize_ticks)
    plt.xticks(rotation=20, ha='right')
    plt.tick_params(axis='y', labelsize=fontsize_ticks)
    plt.margins(x=0.01, y=0.1)
    plt.legend()
    plt.subplots_adjust(bottom=bottom_adjustment)
    plt.savefig(key+save_images)

    # print("\n")




# Creating 7 graphs for apendex
for i in applications:
    app = []
    for j in tools:
        file_name = j+i+'.txt'
        # print(file_name)
        allowed = file_to_list(file_name)
        filtered_dict = {key: [value for value in values if value in allowed] for key, values in complete_data.items()}
        filtered_dicts = dict(sorted(filtered_dict.items()))
        filtered_dict = filtered_dicts

        debloated_dict = {}
        for key, value in filtered_dict.items():
            debloated_dict[key] = len(value)
        debloated_dicts = dict(sorted(debloated_dict.items()))
        debloated_dict = debloated_dicts
        app.append(debloated_dict)
    # print(app)
    
    categories = list(orginal_dict.keys())
    v1 = list(orginal_dict.values())
    values = [list(d.values()) for d in app]
    # print(values)
    # print(v1)
    percentage_reduction = []

    for ii in range(len(values)):
        reduction = [((v1[jj] - values[ii][jj]) / v1[jj] * 100) for jj in range(len(v1))]
        percentage_reduction.append(reduction)
    # print(percentage_reduction)
    values = percentage_reduction

    plt.figure(figsize=(10, 6))
    x = range(len(categories))
    bar_width = 0.2
    for ii, vals in enumerate(values):
        plt.bar(x=np.arange(len(categories)) + ii * bar_width, height=vals, width=bar_width, label=tools[ii])

    plt.xlabel('Systemcall Categories', fontsize = fontsize_labels, fontweight=font_weight)
    plt.ylabel('Percentage Syscalls Reduced', fontsize = fontsize_labels, fontweight=font_weight)
    plt.title('Comparison of syscalls allowed for '+i, fontsize = fontsize_title, fontweight=font_weight)
    plt.xticks(x, categories, fontsize = fontsize_ticks)
    plt.xticks(rotation=20, ha='right')
    plt.margins(x=0.01, y=0.1)
    plt.tick_params(axis='y', labelsize=fontsize_ticks)
    plt.legend()
    plt.subplots_adjust(bottom=bottom_adjustment)
    plt.savefig(i+save_images)




# Creating 3 graphs for case studies
for i in case_study:
    app = []
    for j in tools:
        file_name = j+i+'.txt'
        # print(file_name)
        allowed = file_to_list(file_name)
        filtered_dict = {key: [value for value in values if value in allowed] for key, values in complete_data.items()}
        filtered_dicts = dict(sorted(filtered_dict.items()))
        filtered_dict = filtered_dicts
        # print(filtered_dict)
        app.append(filtered_dict)
    # print("app:",app)
    speaker = app[0]
    confine = app[1]
    slimtoolkit = app[2]
    common = {}
    for key in app[0].keys():
        common_values = set(speaker[key]) & set(confine[key]) & set(slimtoolkit[key])
        common[key] = list(common_values)

    confine_only = {key: list(set(confine[key]) - set(speaker[key]) - set(slimtoolkit[key])) for key in confine}
    speaker_only = {key: list(set(speaker[key]) - set(confine[key]) - set(slimtoolkit[key])) for key in speaker}
    slimtoolkit_only = {key: list(set(slimtoolkit[key]) - set(confine[key]) - set(speaker[key])) for key in slimtoolkit}
    dict_to_excel(confine_only,i+"_confine_only.xlsx")
    dict_to_excel(speaker_only,i+"_speaker_only.xlsx")
    dict_to_excel(slimtoolkit_only,i+"_slimtoolkit_only.xlsx")
    confine_speaker_only = {key: list(set(confine[key]) & set(speaker[key]) - set(slimtoolkit[key])) for key in confine}
    slimtoolkit_speaker_only = {key: list(set(slimtoolkit[key]) & set(speaker[key]) - set(confine[key])) for key in slimtoolkit}
    confine_slimtoolkit_only = {key: list(set(confine[key]) & set(slimtoolkit[key]) - set(speaker[key])) for key in confine}
    dict_to_excel(confine_speaker_only,i+"_confine_speaker_only.xlsx")
    dict_to_excel(slimtoolkit_speaker_only,i+"_slimtoolkit_speaker_only.xlsx")
    dict_to_excel(confine_slimtoolkit_only,i+"_confine_slimtoolkit_only.xlsx")

    # print(common)
    dict_to_excel(common,i+"_common.xlsx")
    debloated_dict = {}
    for key, value in common.items():
        debloated_dict[key] = len(value)
    debloated_dicts = dict(sorted(debloated_dict.items()))
    debloated_dict = debloated_dicts
    # print(debloated_dict)

    categories = list(orginal_dict.keys())
    values = list(debloated_dict.values())
    # print(values)
    
    plt.figure(figsize=(10, 6))
    x = range(len(categories))
    plt.bar(categories, values)

    plt.xlabel('Systemcall Categories',fontsize=fontsize_labels, fontweight=font_weight)
    plt.ylabel('Number of System calls', fontsize=fontsize_labels, fontweight=font_weight)
    plt.title('Common Syscalls retained for '+i, fontsize = fontsize_title, fontweight=font_weight)
    plt.xticks(x, categories, fontsize=fontsize_ticks)
    plt.xticks(rotation=20, ha='right')
    plt.tick_params(axis='y', labelsize=fontsize_ticks)
    plt.margins(x=0.01, y=0.1)
    plt.subplots_adjust(bottom=bottom_adjustment)
    plt.savefig('common_'+i+save_images)