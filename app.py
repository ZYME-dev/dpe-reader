import streamlit as st
import requests

dpe_id = '2369E3640698P'
dpe_id = '2344E0308327N'
dpe_id = st.text_input("Numéro de DPE", value=dpe_id)

b = st.button("Obtenir")
if b:

    url = f"https://observatoire-dpe-audit.ademe.fr/pub/dpe/{dpe_id}/xml"
    headers = {
        'Accept': 'text/xml',
    }

    response = requests.get(url, headers=headers)
    st.write(f"url : `{url}`")
    st.write(response.content)


if __name__ == "__main__":

    dpe_id = '2369E3640698P'
    dpe_id = '2344E0308327N'
    url = f"https://observatoire-dpe-audit.ademe.fr/pub/dpe/{dpe_id}/xml"
    headers = {
        'Accept': 'text/xml',
    }

    def download(url):
        
        # https://stackoverflow.com/questions/2795331/python-download-without-supplying-a-filename
        from urllib.request import urlopen, urlretrieve
        from lxml import etree
        import pyrfc6266
        
        data = urlopen(url)
        info = data.info()
        filename = pyrfc6266.parse_filename(info['Content-Disposition'])
        xmlstring = data.read()
        et = etree.ElementTree(etree.fromstring(xmlstring))
        # et.write('./tmp/output.xml', pretty_print=True)
        root = et.getroot()
        for child in root:
            if child.tag in ["numero_dpe", "statut"] :
                root.remove(child)
            #     continue
            # if True:# TODO: do your check here!
            #     root.remove(child)
        for child in root:
            print(child)
        urlretrieve(url, f'./tmp/{dpe_id}.xml')
        return (xmlstring, et)
        pass

    from bs4 import BeautifulSoup
       
    xmlstring, et = download(url)
    soup = BeautifulSoup(xmlstring, 'xml')
    r1 = soup.find("numero_dpe")
    r2 = soup.find("statut")
    print(r1)
    print(r2)

    with open('tmp/pretty.xml', "w") as f:
        f.write(soup.prettify())
        f.close()

    
    from models_dataclass import Dpe
    from xsdata.formats.dataclass.parsers import XmlParser

    parser = XmlParser()
    result = parser.parse(f'./tmp/{dpe_id}.xml', Dpe)

    murs = result.logement.enveloppe.mur_collection.mur
    for mur in murs:
        print(mur.donnee_entree.surface_paroi_totale)



    # print(f"url : `{url}`")
    # print(response.content)

    # https://www.itersdesktop.com/2020/09/04/downloading-files-in-python-using-requests-module/