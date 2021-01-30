
import os
import pandas as pd
from tqdm import trange

# used for 2013 : KOSSA

def file_search(dirlists, work_dir):


	df = pd.DataFrame()

	for i in trange(0,len(dirlists)):
		work_path = work_dir + "\\"+ dirlists[i]


		if len(work_path) != 0:
			print(work_path)
			temp_df = pd.read_csv(work_path, encoding="cp949")



			####################################################################################

			df = pd.concat([df, temp_df], axis="index")
			print("df row and columns are ", df.shape)
			print("#################### last components in df ####################")
			print("")
			print(df["Component"].tail())



	df.to_csv(work_dir + ".csv", encoding="cp949")
	print("data extracted")






if __name__ == "__main__":

	current_dir = os.path.dirname(os.path.abspath(__file__))
	target_dir = "\\csv\\total"


	work_dir = current_dir + target_dir


	dirlists = os.listdir(work_dir)



	file_search(dirlists, work_dir)
	