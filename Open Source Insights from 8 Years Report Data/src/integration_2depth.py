
import os
import pandas as pd
from tqdm import trange

# integrating all the csv

def file_search(dirlists, work_dir):


	df = pd.DataFrame()

	for i in trange(0,len(dirlists)):
		work_path = work_dir + "\\"+ dirlists[i]


		if os.path.exists(work_path):

			work_files = os.listdir(work_path)

			if len(work_files) != 0:

				for j in range(0, len(work_files)):
					work_path2 = work_path + "\\" + work_files[j]
					print(work_path2)
					temp_df = pd.read_csv(work_path2, encoding="cp949")



					####################################################################################

					df = pd.concat([df, temp_df], axis="index")
					print("df row and columns are ", df.shape)
					print("#################### last components in df ####################")
					print("")
					print(df["Component"].tail())



	df.to_csv("data_integration" + ".csv", encoding="cp949")
	print("data extracted")






if __name__ == "__main__":

	current_dir = os.path.dirname(os.path.abspath(__file__))
	target_dir = "\\csv"

	work_dir = current_dir + target_dir


	dirlists = os.listdir(work_dir)

	file_search(dirlists, work_dir)
	