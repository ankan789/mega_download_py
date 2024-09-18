from mega import Mega
mega = Mega()
m = mega.login("plasma.bit@proton.me", "+r4Cj}_Hd6y'j]U")

print(m.get_user())

## file download
#file = m.find(<file name>)
#m.download(file)

## file upload
#m.upload(<file name>)
