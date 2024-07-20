#Save the data to a CSV file
def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")

    #Table Header
    file.write("Title, Company, Region, Link")
    #Table Contents
    for job in jobs:
        file.write(
            f"{job['title']}, {job['company']}, {job['region']}, {job['link']}")

    file.close()
