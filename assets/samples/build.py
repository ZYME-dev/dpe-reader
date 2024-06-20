import os
import os.path
import sys

cwd = os.getcwd()
sub_dir = os.path.join(cwd, "modules/")
print(sub_dir)
sys.path.append(sub_dir)

import ../../../modules.ademe as ademe

if __name__ == "__main__":

    with open('assets/samples/_list.txt') as f:
        dpe_ids = [line.rstrip() for line in f]

    
    # for id in dpe_ids:
    #     xmlstring = ademe.download_xmlstring(id, f'assets/samples/{id}.xml')
    #     print(id)