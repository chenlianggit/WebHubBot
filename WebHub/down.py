import requests

file_url = "https://ce.phncdn.com/videos/201003/13/1037813/vl_480P_329.0k_1037813.mp4?a5dcae8e1adc0bdaed975f0d67fb5e0527c20903c5bb57a6cad7e6cb50bc41fbb1152c24e90ee7014036ae5e6267673eed4bec51ecadef6a5758c92243e7ac55bb36b6f37267e02e2b2795cb145494477a81739d624bac18ebb73b5ad9c16e38dab80b48346fbfdcf0b3562bda8738a2e4705b170514baa7d7a9610b"

r = requests.get(file_url, stream=True)

with open("python2.mp4", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)

print('完成')
exit()