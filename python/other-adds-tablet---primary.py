# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"50286020","system":"multilex"},{"code":"50620020","system":"multilex"},{"code":"51010020","system":"multilex"},{"code":"51013020","system":"multilex"},{"code":"65635020","system":"multilex"},{"code":"84955020","system":"multilex"},{"code":"84961020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-adds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other-adds-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other-adds-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other-adds-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
