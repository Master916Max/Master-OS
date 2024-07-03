import os

def P4():
     files = ["FS.py", "SFRP.py", "BSR.py",  "FSS.py"]
     data =  ['''import os\nimport time\n\nos.chdir("F://Master1/")\nimport packs.filesystem as fs\nimport packs.KRPU as KRPU\n\ndef setup():\n\tprint("FileSystem is setting up!Please Wait..")\n\ttime.sleep(10)\n\tprint("Setup Completed.")\n\ndef run():\n\twhile KRPU.update():\n\t\tprint("FS: Running")\n\t\ttime.sleep(2)\n''',
              '''import os\ndef P1():\n\tos.chdir("F://Master1/System/KC")\n\tfiles = ["OS.coms", "BS.coms", "WVS.coms"]\n\tfor file in files:\n\t\ttry:\n\t\t\twith open(file, "w")as f:\n\t\t\t\tf.write("")\n\t\t\t\tf.close()\n\t\texcept Exception as e:\n\t\t\treturn e, False\n\treturn "", True        \n\ndef P2():\n\ttry:\n\t\tos.chdir("F://Master1/System/KC")\n\t\treturn P1()\n\texcept FileExistsError or FileNotFoundError:\n\t\ttry:\n\t\t\tos.chdir("F://Master1/System")\n\t\t\tos.mkdir("KC")\n\t\t\treturn P1()\n        \n\t\texcept FileExistsError:\n\t\t\tos.chdir("F://Master1/System")\n\t\t\tos.remove("KC")\n\t\t\tos.mkdir("KC")\n\t\t\treturn P1()''',
              'print("Yes")',
              'print("Yes")']
     os.chdir("C://Master1/System")
     try:
          os.mkdir("KP")
     except FileExistsError:
         pass
     os.chdir("C://Master1/System/KP")
     for fi in files:
         try:
             with open(fi, "w") as f:
                 f.write(data[files.index(fi)])
                 f.close()
         except FileExistsError as e:
             print(e)
             return

     print("Restoration Successfully")

P4()
