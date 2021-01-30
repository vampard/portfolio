
import os
import shutil
import pandas as pd

from tqdm import trange

## 서브단계 파일 상위로 올리고 디렉토리 삭제하는 모듈

def directory_up(dirlists, work_dir):

	
	df = pd.DataFrame()

	for i in trange(0,len(dirlists)):
		work_path = work_dir + "\\"+ dirlists[i]


		if os.path.exists(work_path):

			work_files = os.listdir(work_path)

			if len(work_files) != 0:

				for j in range(0, len(work_files)):
					work_path2 = work_path + "\\" + work_files[j]

					
					############### 파일 이동
					shutil.move(work_path2, work_dir)
					
					print("moved from " + work_path2)
					print("        to " + work_dir)

					############## backup 디렉토리 삭제
					#shutil.rmtree(work_path)


if __name__ == "__main__":

	current_dir = os.path.dirname(os.path.abspath(__file__))
	target_dir = "\\data\\2013\\KOSSA_Dev_Competition"
	work_dir = current_dir + target_dir


	dirlists = os.listdir(work_dir)

	directory_up(dirlists, work_dir)
	


