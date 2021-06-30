#Velocidade da internet

import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
down = round(download)
up = round(upload)
print("Download: {:.2f} Kb".format(down))
print("Upload: {:.2f} Kb".format(up))