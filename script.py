# testing script
import platform, os, subprocess
print('TEST SCRIPT RUN')

def safe_call(cmdString):
	try:
		output = subprocess.check_output(
			cmdString, stderr=subprocess.STDOUT, shell=True,
			universal_newlines=True)
	except subprocess.CalledProcessError as exc:
		print(str(cmdString) + " Status : FAIL", exc.returncode, exc.output)
	else:
		print(str(cmdString) + " Output: \n{}\n".format(output))

'''
GRIDLABD FAIL
-------------
Use command to get required dlls? They're in there.
Create a windows server test env on azure. Windows Server, version 1809. Tried on 1909... worked fine. ARGH!!!
PULL BINARIES!?!?!?! Seems like a longshot since everything's "fine"
Switch to... github actions????
Turns out, running inside command with refreshenv first works. Now, how to do this more generally... just doing it in travis hangs, might need a batch file.
'''

if platform.system()=="Windows":
	print('WINDOWS DETECTED')
	# safe_call('cmd.exe //c RefreshEnv.cmd') #hangs travis
	print('PATH', os.getenv('PATH'))
	print('GLPATH', os.getenv('GLPATH'))
	print(os.listdir('C:\\Program Files\\GridLAB-D\\bin'))
	print(os.listdir('C:\\Program Files\\GridLAB-D\\lib'))
	print(os.listdir('C:\\windows\\system32'))
	safe_call(['C:\\Program Files\\GridLAB-D\\bin\\gridlabd', '-h'])
	# safe_call(['env'])
	safe_call(['gridlabd', '-h'])
	# safe_call('cmd /c "refreshenv && gridlabd -h"')
	# safe_call('cmd /c "gridlabd -h"')
	safe_call(['gridlabd', 'smsSingle.glm'])
	# safe_call('cmd /c "refreshenv && gridlabd smsSingle.glm"')
	# safe_call('cmd /c "refreshenv && SET"')
