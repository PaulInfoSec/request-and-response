import csv
import requests


# open stored CSV of urls to check and store the response status code in output.csv


with open('urls.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Iterate through each line of the csv file
    for row in reader:
        r = requests.get(row['URL'])
        stats = r.status_code
        sites = r.url
        # print(str(stats) + " " + (sites)) 
        with open ('output.csv', 'a') as outf:
            outf.write(str(stats) + "," + (sites) + '\n')

# testing git 


