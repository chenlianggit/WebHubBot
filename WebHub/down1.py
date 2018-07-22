import requests

#file_url = "https://ce.phncdn.com/videos/201003/13/1037813/vl_480P_329.0k_1037813.mp4?a5dcae8e1adc0bdaed975f0d67fb5e0527c20903c5bb57a6cad7e6cb50bc41fbb1152c24e90ee7014036ae5e6267673eed4bec51ecadef6a5758c92243e7ac55bb36b6f37267e02e2b2795cb145494477a81739d624bac18ebb73b5ad9c16e38dab80b48346fbfdcf0b3562bda8738a2e4705b170514baa7d7a9610b"
file_url = "https://de.phncdn.com/videos/201802/05/153408242/480P_600K_153408242.mp4?ttl=1532106693&ri=1843200&rs=960&hash=df0f5e52c9aa64f265b78dd0ce3d9117"
r = requests.get(file_url, stream=True)

with open("python1.mp4", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)

print('success')
exit()
