import os

def renameFiles():
	# get all filenames
	imagesFolder = r"/Users/waylandhe/UdacityFullStackWebDeveloper/ProgrammingFoundationsWithPython/02_Prank/prankImages"
	filenames = os.listdir(imagesFolder)
	os.chdir(imagesFolder)

	# remove all numbers in each of the filenames
	for filename in filenames:
		os.rename(filename, filename.translate(None, "0123456789"))

renameFiles()