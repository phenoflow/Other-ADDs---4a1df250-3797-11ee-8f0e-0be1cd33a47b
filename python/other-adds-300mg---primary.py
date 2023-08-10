# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"68213020","system":"multilex"},{"code":"68484020","system":"multilex"},{"code":"71995020","system":"multilex"},{"code":"72032020","system":"multilex"},{"code":"74665020","system":"multilex"},{"code":"74705020","system":"multilex"},{"code":"78577020","system":"multilex"},{"code":"85247020","system":"multilex"},{"code":"85251020","system":"multilex"},{"code":"86969020","system":"multilex"},{"code":"86971020","system":"multilex"},{"code":"88845020","system":"multilex"},{"code":"9905020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-adds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other-adds-300mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other-adds-300mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other-adds-300mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
