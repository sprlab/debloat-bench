import numpy as np
import matplotlib.pyplot as plt
import pickle
import PyPDF2
from PIL import Image
import matplotlib.backends.backend_pdf as pdf_backend
import os
import glob

png_files = glob.glob('*.png')


png_files = sorted(png_files)


# Print the list of PNG files
print(png_files)

pdf_pages = pdf_backend.PdfPages("report.pdf")



dpi = 350

for i in range(len(png_files)):
    fig1 = plt.figure()
    plt.imshow(plt.imread(png_files[i]))
    plt.axis('off')
    pdf_pages.savefig(fig1, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig1)    


# Close the PDF file
pdf_pages.close()