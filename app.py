import streamlit as st
import requests

dpe_id = '2369E3640698P'
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
    url = f"https://observatoire-dpe-audit.ademe.fr/pub/dpe/{dpe_id}/xml"
    headers = {
        'Accept': 'text/xml',
    }

    def download_1(url):
        # https://stackoverflow.com/questions/2795331/python-download-without-supplying-a-filename
        from urllib.request import urlopen, urlretrieve
        import cgi

        remotefile = urlopen(url)
        contentdisposition = remotefile.info()['Content-Disposition']
        _, params = cgi.parse_header(contentdisposition)
        filename = params["filename"]
        urlretrieve(url, filename)

    download_1(url)

    response = requests.get(url, allow_redirects=True)
    print(response.headers.get('Content-Disposition'))
    # print(f"url : `{url}`")
    # print(response.content)

    # https://www.itersdesktop.com/2020/09/04/downloading-files-in-python-using-requests-module/