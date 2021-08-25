import csv

dataset_1 = []
dataset_2 = []

with open('dataset_1.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open('dataset_2.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

header_1 = dataset_1[0]
stars_data_1 = dataset_1[1:]

header_2 = dataset_2[0]
stars_data_2 = dataset_2[1:]

headers = header_1 + header_2
stars_data = []

for index, data_row in enumerate(stars_data_1) :
    stars_data.append(stars_data_1[index] + stars_data_2[index])

with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data) 