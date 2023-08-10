# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"74026020","system":"multilex"},{"code":"74033020","system":"multilex"},{"code":"74668020","system":"multilex"},{"code":"74684020","system":"multilex"},{"code":"74689020","system":"multilex"},{"code":"74702020","system":"multilex"},{"code":"74708020","system":"multilex"},{"code":"74967020","system":"multilex"},{"code":"74977020","system":"multilex"},{"code":"76512020","system":"multilex"},{"code":"87476020","system":"multilex"},{"code":"87478020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-adds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["orodispersible-other-adds---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["orodispersible-other-adds---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["orodispersible-other-adds---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
