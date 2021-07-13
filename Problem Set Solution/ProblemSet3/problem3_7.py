import csv
def problem3_7(csv_pricefile, flower):
    f = open(csv_pricefile)
    reader = csv.reader(f)
    for line in reader:
        if line[0] == flower:
            print(line[1])