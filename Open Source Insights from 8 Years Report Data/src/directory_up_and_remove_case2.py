
import os
import shutil


## 서브단계 파일 상위로 올리고 backup 디렉토리 삭제하는 모듈

def del_backup(dirlists, upstair_path):

	for i in range(0,len(dirlists)):

		srcPath1 = str(dirlists[i]) + "\\" + upstair_path
		movePath = cu_dir + "\\" + srcPath1 + "\\"

		#백업디렉토리가 있으면?
		if os.path.exists(movePath):

			#리스트 반환
			dirlists2 = os.listdir(movePath)

			for j in range(0, len(dirlists2)):
				# 이동할 파일리스트 반환
				movefile = movePath + dirlists2[j]
				# 이동 경로 반환
				dstPath = cu_dir + "\\" + str(dirlists[i]) + "\\"
				

				############### 파일 이동
				shutil.move(movefile, dstPath)
				
				print("moved from " + movePath)
				print("        to " + dstPath)

			############## backup 디렉토리 삭제
			shutil.rmtree(movePath)



def del_frontFiles(dirlists, exception_path):
	for i in range(0,len(dirlists)):

		srcPath1 = str(dirlists[i]) + "\\"
		scanPath = cu_dir + "\\" + srcPath1 

		#백업디렉토리가 있으면?
		if os.path.exists(scanPath):
			#리스트 반환
			dirlists2 = os.listdir(scanPath)

			if "backup" in dirlists2:
				print("Yes I have")
				dirlists2.remove('backup')
				if dirlists2 ==[]:
					print("No file in this directory")

				else:

					for j in range(0, len(dirlists2)):

						# 삭제할 파일리스트 반환
						delfiles = scanPath + dirlists2[j]
						print("Delete " + delfiles)
						os.remove(delfiles)
						
			else:
				print("No I don't")






if __name__ == "__main__":

	cu_dir = os.path.dirname(os.path.abspath(__file__))
	searchObjects = "\\2018\\1. 공개SW 검증(NIPA)\\0. 기업"


	cu_dir = cu_dir + searchObjects

	upstair_path = "backup" 
	exception_path = "backup"

	dirlists = os.listdir(cu_dir)

	#backup폴더를 제외한 모든 파일 삭제
	# del_frontFiles(dirlists, exception_path)
	#backup폴더의 원본 파일을 상위로 이동시키기
	del_backup(dirlists, upstair_path)
	