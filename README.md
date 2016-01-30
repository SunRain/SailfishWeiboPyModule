# SailfishWeiboPyModule
Py module for SailfishWeibo

A py module for https://github.com/SunRain/SailfishWeibo ,use this module can login with your username and password

##Requires:
* pycurl
* rpweibo

##Usage:
<code>pageStack.push(Qt.resolveUrl("LoginComponent.qml"))</code>
or <code><code>pageStack.push(Qt.resolveUrl("LoginComponent.qml"),{"API_KEY:"","API_SECRET":"","REDIRECT_URI":""})</code>

##Note:
Here's how you configure Qt Creator to build the project in windows:

1. Open the .pro file in Qt Creator

2. Modify the project build settings:
	Build Steps:

		add a new one:

		Custom Process Step

				  Command: $full_path_to/build-win-$target.cmd
							note: (for i486, $target is i486, for arm, $target is armv7hl)
								  You may need to modify the cmd file to fit your environment
				Arguments: 
		Working directory: %{buildDir}
		
		move this custom process step up, the build steps will be like this:
		1. start sdk
		2. custom process
		3. qmake
		4. make