''' Name: David Mendoza 
    Date Created: March 1, 2022
    Date Last Modified: March 4, 2022
    Objective: To use Matplotlib in conjunction with Pandas to 
    be able to plot in a 3d plane by providing the file name and 
    attributes looking to graph. 
    
    Before executing script: Install matplotlib and pandas. Have both libraries 
    in the correct file path. If not done right, ModuleNotFoundError is likely to 
    be the error 
	
	Other errors that can cause the program to crash are:
	1. Not providing the correct file with the appropriate file extension 
	2. Forgetting to exhange target value with the appropriate attribute names
	3. Other case could be not cleaning your data properly. Having text or Null 
	values will cause the program to end without producing a graph 

	If you like to learn more about matplotlib: 
	https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.scatter.html
''' 

try:
	import matplotlib.pyplot as plt
	import pandas as pd

	is_imported = True
except Exception as e:
	is_imported = False
	print('You could not import matplotlib or pandas')

def main():
	if is_imported:
		try:
			file_name = "file_name.csv"
			fig = plt.figure()
			ax = fig.add_subplot(projection='3d')
			
			data = pd.read_csv(file_name, index_col=False, delimiter=',')
			# get column names 
			# go through each
			target_values = ['attribute_1', 'attribute_2', 'attribute_3']
			data_to_plot = data.loc[:, target_values]
			
			coordinate = []

			for posit in data_to_plot.index:
				for attrib in data_to_plot.columns:
					coordinate.append(data_to_plot[attrib][posit])
				
				ax.scatter(coordinate[0],coordinate[1], coordinate[2], c='#000000' ,marker='o')
				coordinate = []
			

			ax.set_xlabel('Saturated Fat (g)')
			ax.set_ylabel('Sugar (g)')
			ax.set_zlabel('Fiber (g)')

			plt.show()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()