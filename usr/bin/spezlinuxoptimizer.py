import psutil, os, time

time.sleep(10)

ram = str(psutil.virtual_memory())
ram = ram.replace("svmem(total=", "")
ram = ram.replace(", ", "\n")
ram = ram.split("\n", 1)[0]
ram = int(ram)
print(ram)

if ram > 3000000000:
  print("Passed.")
  os.system("gnome-shell-extension-tool --enable blyr@yozoon.dev.gmail.com")
  os.system("gnome-shell-extension-tool --enable window-corner-preview@fabiomereu.it")
  os.system("rm -rf /home/$USERNAME/.config/autostart/spezlinuxoptimizer.desktop")
else:
  print("Failed.")
  os.system("gnome-shell-extension-tool --disable blyr@yozoon.dev.gmail.com")
  os.system("gnome-shell-extension-tool --disable window-corner-preview@fabiomereu.it")
  os.system("gnome-shell-extension-tool --disable blyr@yozoon.dev.gmail.com")
  os.system("gnome-shell-extension-tool --disable window-corner-preview@fabiomereu.it")
  os.system("gnome-shell-extension-tool --disable blyr@yozoon.dev.gmail.com")
  os.system("gnome-shell-extension-tool --disable window-corner-preview@fabiomereu.it")
  os.system("notify-send -t 100 'IMPORTANT INFORMAITON' 'Some features (Picture in picture etc.) have been disabled for optimization purposes. You can open it from Tweaks, but your machine may freeze because of excessive memory usage.'")
  os.system("rm -rf /home/$USERNAME/.config/autostart/spezlinuxoptimizer.desktop")
