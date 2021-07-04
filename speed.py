#Velocidade da internet

import speedtest

test = speedtest.Speedtest()
download = test.download()
rsdown = round(download)
fdown = int(rsdown / 1e+6)
upload = test.upload()
rsup = round(upload)
fup = int(rsup / 1e+6)
print(f"Download: {fdown} Mb/s")
print(f"Upload: {fup} Mb/s")
