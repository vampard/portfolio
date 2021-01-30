
import os
import pandas as pd
from tqdm import trange

# used for 2017 : SK주식회사

def file_search(dirlists, work_dir):


	df = pd.DataFrame()

	for i in trange(0,len(dirlists)):
		work_path = work_dir + "\\"+ dirlists[i]


		if len(work_path) != 0:

			temp_df = pd.read_excel(work_path, sheet_name='Bill of Materials', skiprows=[0], encoding="cp949")
			temp_df.loc[temp_df["License Conflict"].isnull(),"License Conflict"] = "프로젝트명"
			project_license = temp_df.loc[temp_df["License Conflict"] == "프로젝트명","License"]
			
			# additional info
			ad_info = work_path.strip().split('\\')
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


	
	df['Code Match'] = df['# Manual Code Match'] + df['# Rapid ID Code Match']

	df = df[['Project Index','License Conflict', 'Component', 'Version', 'Home Page', 'License', 'Usage', 'Code Match', 'year', 'service', 'customer', 'project license','file']]

	df.to_csv(work_dir + ".csv", encoding="cp949")
	print("data extracted")






if __name__ == "__main__":

	current_dir = os.path.dirname(os.path.abspath(__file__))
	target_dir = "\\data\\2017\\Audit_Service\\SK주식회사"


	work_dir = current_dir + target_dir


	dirlists = os.listdir(work_dir)

	print("dirlist ----->", work_dir)

	file_search(dirlists, work_dir)
	