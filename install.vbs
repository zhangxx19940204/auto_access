set objshell=createobject("wscript.shell")

objshell.run("%comspec% /k python -m pip install --upgrade pip && pip install -U wxpy"),1,true