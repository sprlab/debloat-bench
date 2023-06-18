
import numpy as np
import matplotlib.pyplot as plt
import pickle
import PyPDF2
from PIL import Image
import matplotlib.backends.backend_pdf as pdf_backend
import os


with open('temp.pkl', 'rb') as f:
        data = pickle.load(f)

# print("data: ",data)
# print("len(data): ",len(data))
# Sys Calls Reduced


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("---------------------")


def extract_sys(dictionary):
    app_names = []
    syscalls = []

    for key, value in dictionary.items():
        app_names.append(key)
        for item in value:
            for sub_key, sub_value in item.items():
                if sub_key == 'syscall':
                    syscalls.append(sub_value)
    return app_names, syscalls

def extract_size(dictionary):
    app_names = []
    szie = []

    for key, value in dictionary.items():
        app_names.append(key)
        for item in value:
            for sub_key, sub_value in item.items():
                if sub_key == 'size':
                    szie.append(sub_value)
    return app_names, szie

def extract_correctness(dictionary):
    app_names = []
    correctness = []

    for key, value in dictionary.items():
        app_names.append(key)
        for item in value:
            for sub_key, sub_value in item.items():
                if sub_key == 'correctness':
                    correctness.append(sub_value)
    return app_names, correctness

def extract_cves(dictionary):
    app_names = []
    cves = []

    for key, value in dictionary.items():
        app_names.append(key)
        for item in value:
            for sub_key, sub_value in item.items():
                if sub_key == 'CVEs':
                    cves.append(sub_value)
    return app_names, cves



def single_syscalls(list1,list2,tool):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        plt.bar(list1, list2, width = 0.50, edgecolor ='grey')
        plt.xlabel('Applications',  fontweight ='bold', fontsize = 15)
        plt.ylabel('Number of Syscalls blocked', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(list1))], list1, fontsize=20)
        plt.title(tool, fontweight ='bold', fontsize = 15)
        plt.savefig("single_syscall_graph.png")

def syscalls(speaker,slimtoolkit,applications):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        br1 = np.arange(len(speaker))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        plt.bar(br1, speaker, color ='r', width = 0.15, edgecolor ='grey', label ='speaker')
        plt.bar(br2, slimtoolkit, color ='g', width = 0.15, edgecolor ='grey', label ='slimtoolkit')
        plt.xlabel('Applications', fontweight ='bold', fontsize = 15)
        plt.ylabel('Number of Syscalls blocked', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(speaker))], applications, fontsize=20)
        plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
        plt.savefig("syscall_graph.png")

def single_correctness(list1,list2,tool):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        plt.bar(list1, list2, width = 0.50, edgecolor ='grey')
        plt.xlabel('Applications', fontweight ='bold', fontsize = 15)
        plt.ylabel('Correct Test Cases', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(list1))], list1, fontsize=20)
        plt.title(tool, fontweight ='bold', fontsize = 15)
        plt.savefig("single_correctness_graph.png")

def correctness(speaker,slimtoolkit,applications):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        br1 = np.arange(len(speaker))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        plt.bar(br1, speaker, color ='r', width = 0.15, edgecolor ='grey', label ='speaker')
        plt.bar(br2, slimtoolkit, color ='g', width = 0.15, edgecolor ='grey', label ='slimtoolkit')
        plt.xlabel('Applications', fontweight ='bold', fontsize = 15)
        plt.ylabel('Correct Test Cases', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(speaker))], applications, fontsize=20)
        plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
        plt.savefig("correctness_graph.png")


def single_CVEs(list1,list2,tool):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        plt.bar(list1, list2, width = 0.50, edgecolor ='grey')
        plt.xlabel('Applications',  fontweight ='bold', fontsize = 15)
        plt.ylabel('CVEs Mitigated',  fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(list1))], list1, fontsize=20)
        plt.title(tool,  fontweight ='bold', fontsize = 15)
        plt.savefig("single_cves_graph.png")


def CVEs(speaker,slimtoolkit,applications):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        br1 = np.arange(len(speaker))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        plt.bar(br1, speaker, color ='r', width = 0.15, edgecolor ='grey', label ='speaker')
        plt.bar(br2, slimtoolkit, color ='g', width = 0.15, edgecolor ='grey', label ='slimtoolkit')
        plt.xlabel('Applications', fontweight ='bold', fontsize = 15)
        plt.ylabel('CVEs Mitigated', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(speaker))], applications, fontsize=20)
        plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
        plt.savefig("cves_graph.png")

def Size(original,debloated,applications):
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        br1 = np.arange(len(original))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        plt.bar(br1, original, color ='r', width = 0.15, edgecolor ='grey', label ='original size')
        plt.bar(br2, debloated, color ='g', width = 0.15, edgecolor ='grey', label ='debloated size')
        plt.xlabel('Applications', fontweight ='bold', fontsize = 15)
        plt.ylabel('Size Reduction', fontweight ='bold', fontsize = 15)
        plt.title("Slimtoolkit", fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(original))], applications, fontsize=20)
        plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
        plt.savefig("size_graph.png")


def create_pdf_with_graphs(file1, file2, file3, file4, output_file):
    # Set the DPI (dots per inch) value for saving images
    dpi = 300

    # Create a PDF backend
    pdf_pages = pdf_backend.PdfPages(output_file)

    # Add Graph 1
    fig1 = plt.figure()
    plt.imshow(plt.imread(file1))
    plt.axis('off')
    pdf_pages.savefig(fig1, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig1)

    # Add Graph 2
    fig2 = plt.figure()
    plt.imshow(plt.imread(file2))
    plt.axis('off')
    pdf_pages.savefig(fig2, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig2)

    # Add Graph 3
    fig3 = plt.figure()
    plt.imshow(plt.imread(file3))
    plt.axis('off')
    pdf_pages.savefig(fig3, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig3)

    # Add Graph 4
    fig3 = plt.figure()
    plt.imshow(plt.imread(file4))
    plt.axis('off')
    pdf_pages.savefig(fig3, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig3)

    # Close the PDF file
    pdf_pages.close()


def create_pdf_with_graphs2(file1, file2, file3, output_file):
    # Set the DPI (dots per inch) value for saving images
    dpi = 300

    # Create a PDF backend
    pdf_pages = pdf_backend.PdfPages(output_file)

    # Add Graph 1
    fig1 = plt.figure()
    plt.imshow(plt.imread(file1))
    plt.axis('off')
    pdf_pages.savefig(fig1, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig1)

    # Add Graph 2
    fig2 = plt.figure()
    plt.imshow(plt.imread(file2))
    plt.axis('off')
    pdf_pages.savefig(fig2, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig2)

    # Add Graph 3
    fig3 = plt.figure()
    plt.imshow(plt.imread(file3))
    plt.axis('off')
    pdf_pages.savefig(fig3, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig3)

    # Close the PDF file
    pdf_pages.close()



if len(data)>1:
        app, syst = extract_sys(list(data[0].values())[0])
        speaker_syscalls = syst
        app, syst = extract_sys(list(data[1].values())[0])
        slimtoolkit_syscalls = syst

        app, syst = extract_correctness(list(data[0].values())[0])
        speaker_correctness = syst
        app, syst = extract_correctness(list(data[1].values())[0])
        slimtoolkit_correctness = syst

        app, syst = extract_cves(list(data[0].values())[0])
        speaker_cves = syst
        app, syst = extract_cves(list(data[1].values())[0])
        slimtoolkit_cves = syst

        app, syst = extract_size(list(data[1].values())[0])
        slimtoolkit_size = syst
        original_size, Debloated_size = zip(*slimtoolkit_size)
        original_size = list(original_size)
        Debloated_size = list(Debloated_size)

        # print(speaker_syscalls,speaker_cves,speaker_correctness)
        # print(slimtoolkit_syscalls,slimtoolkit_cves,slimtoolkit_correctness)
        # print(slimtoolkit_size)
        syscalls(speaker_syscalls,slimtoolkit_syscalls,app)
        correctness(speaker_correctness,slimtoolkit_correctness, app)
        CVEs(speaker_cves,slimtoolkit_cves,app)
        Size(original_size,Debloated_size,app)

        create_pdf_with_graphs("syscall_graph.png","correctness_graph.png","cves_graph.png","size_graph.png","report.pdf")
        delete_file("correctness_graph.png")
        delete_file("cves_graph.png")
        delete_file("syscall_graph.png")
        delete_file("size_graph.png")
        delete_file("slim.report.json")
        delete_file("temp.pkl")
        print("*****REPORT CREATED*****")

if len(data) == 1:
        # print("here")
        # print(data)
        if list(data.keys())[0] == "slimtoolkit":
                app = list(data['slimtoolkit'].keys())
                slimtoolkit_syscalls = [app[0]['syscall'] for app in data['slimtoolkit'].values()]
                slimtoolkit_correctness = [app[1]['correctness'] for app in data['slimtoolkit'].values()]
                slimtoolkit_cves = [app[2]['CVEs'] for app in data['slimtoolkit'].values()]
                slimtoolkit_size = [app[3]['size'] for app in data['slimtoolkit'].values()]
                original_size, Debloated_size = zip(*slimtoolkit_size)
                original_size = list(original_size)
                Debloated_size = list(Debloated_size)
                # print(app, slimtoolkit_syscalls)
                # print(slimtoolkit_cves)
                # print(slimtoolkit_correctness)
                # print(slimtoolkit_size)

                single_syscalls(app,slimtoolkit_syscalls,'slimtoolkit')
                single_CVEs(app, slimtoolkit_cves,'slimtoolkit')
                single_correctness(app,slimtoolkit_correctness,'slimtoolkit')
                Size(original_size,Debloated_size,app)
                create_pdf_with_graphs("single_syscall_graph.png","single_correctness_graph.png","single_cves_graph.png","size_graph.png","report.pdf")
                delete_file("single_correctness_graph.png")
                delete_file("single_cves_graph.png")
                delete_file("single_syscall_graph.png")
                delete_file("size_graph.png")
                delete_file("slim.report.json")
                delete_file("temp.pkl")
                print("*****REPORT CREATED*****")
        elif list(data.keys())[0] == "speaker":
                app = list(data['speaker'].keys())
                speaker_syscalls = [app[0]['syscall'] for app in data['speaker'].values()]
                speaker_correctness = [app[1]['correctness'] for app in data['speaker'].values()]
                speaker_cves = [app[2]['CVEs'] for app in data['speaker'].values()]

                # print(app, speaker_syscalls)
                # print(speaker_cves)
                # print(speaker_correctness)

                single_syscalls(app,speaker_syscalls,'Speaker')
                single_CVEs(app, speaker_cves,'Speaker')
                single_correctness(app,speaker_correctness,'Speaker')
                
                create_pdf_with_graphs2("single_syscall_graph.png","single_correctness_graph.png","single_cves_graph.png","report.pdf")
                delete_file("single_correctness_graph.png")
                delete_file("single_cves_graph.png")
                delete_file("single_syscall_graph.png")
                delete_file("slim.report.json")
                # delete_file("temp.pkl")
                print("*****REPORT CREATED*****")
