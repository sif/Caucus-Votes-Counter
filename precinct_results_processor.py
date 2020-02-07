# Sifer Aseph, Jeff Richman
# Caucus Votes Counter

import csv

with open('Iowa Caucus Tally Demonstration.csv') as result_file:
    read_csv = csv.reader(result_file, delimiter=',')
    result_data = list(read_csv)

with open('Master.csv') as master_file:
    read_csv = csv.reader(master_file, delimiter=',')
    master_data = list(read_csv)

total_count = 0
joe_biden_count = 0
pete_buttigieg_count = 0
elizabeth_warren_count = 0
bernie_sanders_count = 0
amy_klobuchar_count = 0

new_contact_list = []

for result_itr in range(1, len(result_data)):
    result = result_data[result_itr]
    result_auth1 = result[3]
    result_auth2 = result[4]
    result_id = result[2]

    master = master_data[int(result_id)]
    master_auth1 = master[7]
    master_auth2 = master[8]
    print("checking master[" + str(int(result_id)) + "] with auth '" + master_auth1 + "' and '" + master_auth2 + "' against '" + result_auth1 + "' and '" + result_auth2 + "'")
    if ((result_auth1 == master_auth1) and (result_auth2 == master_auth2)) or ((result_auth1 == master_auth2 and result_auth2 == master_auth1)):
        joe_biden_count = int(result[7])
        pete_buttigieg_count = int(result[8])
        elizabeth_warren_count = int(result[9])
        bernie_sanders_count = int(result[10])
        amy_klobuchar_count = int(result[11])
        total_count = joe_biden_count + pete_buttigieg_count + elizabeth_warren_count + bernie_sanders_count + amy_klobuchar_count

        master[9] = joe_biden_count
        master[10] = pete_buttigieg_count
        master[11] = elizabeth_warren_count
        master[12] = bernie_sanders_count
        master[13] = amy_klobuchar_count

        print("County: " + master[1])
        print("Location Name: " + master[3] + " (" + master[4] + ")")
        print("Count for Biden: " + str(joe_biden_count))
        print("Count for Buttigieg: " + str(pete_buttigieg_count))
        print("Count for Warren: " + str(elizabeth_warren_count))
        print("Count for Sanders: " + str(bernie_sanders_count))
        print("Count for Klobuchar: " + str(amy_klobuchar_count))
        print("Total count: " + str(total_count))
        print()

    else:
        new_contact_file_row = ["Authentication problem:", result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11]]
        new_contact_list.append(new_contact_file_row)

        print("Irregularity detected at " + master[3] + " (" + master[4] + ")")
        print("Flagged: " + master[1])
        print("Please contact " + result[5] + " at:")
        print("Email: " + result[1])
        print("Phone: " + result[6])

with open("master_results.csv", "w", newline='') as master_results_file:
    writer_master_results_csv = csv.writer(master_results_file)
    writer_master_results_csv.writerows(master_data)

with open("CONTACT IMMEDIATELY.csv", "w", newline='') as contact_file:
    writer_contact_csv = csv.writer(contact_file)
    writer_contact_csv.writerows(new_contact_list)
