# bearly dancing ![](https://github.com/oflatt/portfolio-gifs/blob/master/beardance.gif)
A rhythm rpg with randomly generated beatmaps, written in python using the pygame library. Journey through a quirky world, playing the music for dance battles between a bear and his foes.

## setting up the environment

Install python 3.

Make sure that pip is installed- type pip (or try pip3)

Run python setup.py.

Do not run setup.py from IDLE- there seems to be a bug that causes ultra-slow download speeds.

To play the game without development features, set exportmode in variables.py to True.

## building an executable

Windows:

Call **python build.py build**.
A folder named build should appear.

Mac:

Call **python build.py bdist_mac --iconfile icon.icns**.
A folder named build should appear. If there are errors in copying files (such as wav or png) or errors in included libraries, there may be no effect.



![](https://github.com/oflatt/portfolio-gifs/blob/master/bearly-dancing-demo.gif)


<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">bearly dancing</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Oliver Flatt</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

