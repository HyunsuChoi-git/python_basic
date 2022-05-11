
writeTemplate = "- {0} 주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : "

for i in range(1, 51) :
    with open("{0}주차.txt".format(i), "w", encoding="UTF8") as text_file :
        text_file.write(writeTemplate.format(i))
