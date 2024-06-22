import os
import os.path
import sys
import dpe.ademe as ademe


# sub_dir = os.path.join(cwd, "modules/")
# print(sub_dir)
# sys.path.append(sub_dir)



if __name__ == "__main__":

    print("")
    cwd = os.getcwd()
    print(cwd)

    with open('./assets/samples/_list.txt') as f:
        dpe_ids = [line.rstrip() for line in f]

    
    for id in dpe_ids:
        xmlstring = ademe.download_xmlstring(id, f'assets/samples/{id}.xml')
        print(id)