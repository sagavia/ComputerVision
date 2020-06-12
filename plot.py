
import matplotlib.pyplot as plt



def plotArray(img, title, rows, cols,fsize,font=30):
	#this takes a list of images and a list of titles and displays it in
	#a rows by columns array
			
	fig, ax = plt.subplots(rows, cols, figsize = fsize)
	cnt = 0
	for ro in range(rows):
		for co in range(cols):
			ax[ro,co].imshow(img[cnt], cmap='gray')
			ax[ro,co].set_title(title[cnt], fontsize=font)
			ax[ro,co].axis('off')
			cnt = cnt + 1
	plt.tight_layout()
	plt.show()
	
def plotArray1Row(img, title,cols, fsize,font=30):
	fig, ax = plt.subplots(1, cols, figsize = fsize)
	for co in range(cols):
		ax[co].imshow(img[co],cmap='gray')
		ax[co].set_title(title[co], fontsize=font)
		ax[co].axis('off')
	plt.tight_layout()
	plt.show()
	

