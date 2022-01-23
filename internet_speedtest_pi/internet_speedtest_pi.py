import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import speedtest

# initialize speedtest
test = speedtest.Speedtest()

# test speed and convert to Mbps
download_speed = test.download() / 1024**2
upload_speed = test.upload() / 1024**2

# get ping in ms
ping = test.results.ping


print("break")
breakpoint()
