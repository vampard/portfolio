
import os
import pandas as pd
import numpy as np
from tqdm import trange

# used for 2017 : kosslab

def file_search(dirlists, work_dir):

	
	df = pd.DataFrame()

	for i in trange(0,len(dirlists)):
		work_path = work_dir + "\\"+ dirlists[i]

		print(work_path)
		if len(work_path) != 0:

			
			temp_df = pd.read_excel(work_path, sheet_name='프로젝트 구성요소 목록(Bill of Materials)', skiprows=[0], encoding="cp949")

			temp_df.loc[temp_df["준법성 현황"].isnull(),"준법성 현황"] = "프로젝트명"
			project_license = temp_df.loc[temp_df["준법성 현황"] == "프로젝트명","라이선스"]

			# additional info
			ad_info = work_path.strip().split('\\')
			print(ad_info)
			temp_df["year"] = ad_info[6]
			temp_df["service"] = ad_info[7]
			
			temp_df["customer"] = ad_info[7]
			temp_df["project license"] = project_license.loc[project_license.index[0]]
			temp_df["file"] = ad_info[8]
			print(temp_df.columns)

			df = pd.concat([df, temp_df], axis="index")
			print("df row and columns are ", df.shape)
			# print("#################### last components in df ####################")
			print("")

			print(df["컴포넌트"].tail())





	df = df.rename(columns={'준법성 현황':'License Conflict', '컴포넌트':'Component', '버전':'Version',\
    '홈페이지':'Home Page', '라이선스':'License', '결합형태':'Usage', '해당파일 수':'Code Match'})


	if '소스코드 공개필요' in df.columns:
		df = df.drop('소스코드 공개필요', axis="columns")

	if '다운로드' in df.columns:
		df = df.drop('다운로드', axis="columns")

	if '특허보복조항' in df.columns:
		df = df.drop('특허보복조항', axis="columns")


	df = df.reset_index().rename(columns={'index':'Project Index'})


	df = df[['Project Index','License Conflict', 'Component', 'Version', 'Home Page', 'License', 'Usage', 'Code Match', 'year', 'service', 'customer', 'project license','file']]
	df.loc[df['Component'].isnull(),"Component"] = "unspecified"


	df.to_csv(work_dir + ".csv", encoding="cp949")
	print("data extracted")





if __name__ == "__main__":

	current_dir = os.path.dirname(os.path.abspath(__file__))
	target_dir = "\\data\\2017\\NIPA_Kosslab"
	work_dir = current_dir + target_dir


	dirlists = os.listdir(work_dir)

	file_search(dirlists, work_dir)
	