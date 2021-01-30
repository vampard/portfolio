
import os
import pandas as pd
from tqdm import trange

# used for 2014 : NIPA Support, NIPA Individual, NIPA University, NIPA Company, Sales, SK플래닛

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
					temp_df = pd.read_excel(work_path2, sheet_name='Bill of Materials', skiprows=[0], encoding="cp949")

					temp_df.loc[temp_df["License Conflict"].isnull(),"License Conflict"] = "프로젝트명"
					project_license = temp_df.loc[temp_df["License Conflict"] == "프로젝트명","License"]

					# additional info
					ad_info = work_path2.strip().split('\\')
					print(ad_info)
					temp_df["year"] = ad_info[6]
					temp_df["service"] = ad_info[7]
					temp_df["customer"] = ad_info[8]
					temp_df["project license"] = project_license.loc[project_license.index[0]]
					temp_df["file"] = ad_info[9]


					######################### 이 부분이 결측치 해결에 결정적인 역할을 함 #################

					# data preprocessing
					
					try:
						temp_df['# Manual Code Match'] = temp_df['# Manual Code Match'].fillna(0).astype(int)
					except Exception as ex:
						print('error occurred -----------------> ', ex)	
						temp_df['# Manual Code Match'] = temp_df['# Manual Code Match'].str.replace(',','').fillna(0).astype(int)	

					try:
						temp_df['# Rapid ID Code Match'] = temp_df['# Rapid ID Code Match'].fillna(0).astype(int)
					except Exception as ex:
						print('error occurred -----------------> ', ex)	
						temp_df['# Rapid ID Code Match'] = temp_df['# Rapid ID Code Match'].str.replace(',','').fillna(0).astype(int)	


					####################################################################################

					df = pd.concat([df, temp_df], axis="index")
					print("df row and columns are ", df.shape)
					print("#################### last components in df ####################")
					print("")
					print(df["Component"].tail())




	df = df.reset_index().rename(columns={'index':'Project Index'})
	print("is Ship included? ", df['Ship Status'].unique())
	if 'Ship' in df['Ship Status'].unique():

		df['Code Match'] = df['# Manual Code Match'] + df['# Rapid ID Code Match']	
	
	else:
		df['Code Match'] = df['Ship Status'] +  df['# Manual Code Match'] + df['# Rapid ID Code Match']

	df = df[['Project Index','License Conflict', 'Component', 'Version', 'Home Page', 'License', 'Usage', 'Code Match', 'year', 'service', 'customer', 'project license','file']]

	df.to_csv(work_dir + ".csv", encoding="cp949")
	print("data extracted")






if __name__ == "__main__":

	current_dir = os.path.dirname(os.path.abspath(__file__))
	target_dir = "\\data\\2014\\Sales"

	work_dir = current_dir + target_dir


	dirlists = os.listdir(work_dir)

	file_search(dirlists, work_dir)
	