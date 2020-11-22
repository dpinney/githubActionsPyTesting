import platform, os, time
#  install script
print('INSTALL RUNNING')

# macos brew testing
if platform.system()=="Darwin": # MacOS
	# os.system("brew install wget ffmpeg git graphviz octave mdbtools") # fails, kills python
	# os.system("brew install wget ffmpeg git graphviz octave mdbtools; brew link --overwrite python3") # works, extra 5 minutes
	os.system("HOMEBREW_NO_AUTO_UPDATE=1 brew install wget ffmpeg git graphviz octave mdbtools") # works, fast
	# SPLAT TEST
	os.system("wget https://www.qsl.net/kd2bd/splat-1.4.2-osx.tgz")
	os.system("sudo tar -xvzf splat-1.4.2-osx.tgz")
	os.system('''
		cd splat-1.4.2;
		sed -i '' 's/ans=""/ans="2"/g' configure;
		sudo bash configure;
	''')

if platform.system()=="Windows":
	os.system("choco install -y wget")
	os.system("choco install -y vcredist-all")
	os.system("wget --no-check-certificate https://sourceforge.net/projects/gridlab-d/files/gridlab-d/Candidate%20release/gridlabd-4.0_RC1.exe")
	os.system("gridlabd-4.0_RC1.exe/silent")
	# time.sleep(10)
	# os.system('powershell "./gridlabd-4.0_RC1.exe /silent"')
	# os.system("choco install -y mingw")
	# os.system("choco install -y cygwin")
	# os.system("choco install -y gnuplot")
	# os.system("gridlabd-4.0_RC1.exe /silent")
