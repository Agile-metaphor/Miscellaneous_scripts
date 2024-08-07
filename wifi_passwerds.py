import subprocess
try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
            r = "{:<30}|  {:<}".format(i, results[0])
            file = open('./wifi_passwords.txt', 'a', encoding="utf-8")
            file.write(r)
            file.write("\n")
            file.close()
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
except subprocess.CalledProcessError:
	print("Encoding Error Occurred")