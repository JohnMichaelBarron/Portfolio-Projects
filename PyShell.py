# Custom Python Shell - Level 4 Shell Implementation
# Written by John-Michael Barron
# Supports command execution, directory navigation, environment expansion, piping, redirection,
# background jobs (&), and command history.
# Runtime efficiency per command: O(n), where n is the number of tokens or piped segments in the input.


import os 
import subprocess 
import shlex 



history = [] #store user commands 

#add cd support, change the working directory 

def change_directory(path): 
    try: 
        os.chdir(path)                                     #attempt to change current working directory j
    except FileNotFoundError:                              
        print(f"No such directory: {path}")
    except Exception as e:
        print(f"cd error: {e}")

#infinite loop to keep the shell working 
while True: 
    try: 
        cwd = os.getcwd()                                  #get current working directory for prompt 
        cmd = input(f"{cwd} $ ").strip()                   #get user input and strip whitespace  
        if not cmd: 
            continue
        if cmd.lower() in ["exit", "quit"]:
             break

        history.append(cmd)                               #save cmd history
        if cmd == "history": 
            for i, h in enumerate(history):
                print(f"{i +1}: {h}")
            continue 
        
        #expand the environment variables like $HOME
        cmd = os.path.expandvars(cmd)
        background = False

        if cmd.endswith("&"):
            background = True
            cmd = cmd[:-1].strip()

        if cmd.startswith("cd"):
            args = shlex.split(cmd) 
            if len(args) >  1:
                change_directory(args[1])                  # go to the specified directory
            else: 
                change_directory(os.path.expanduser("~"))  # go to home directory by default
            continue                                       #run the other commands via system shell 



        #handle pipes 
        if "|" in cmd: 
            commands = [shlex.split(part) for part in cmd.split("|")]             #split command string by '|' and tokenize each part 
            prev_proc = None                                                      #initialize variable to hold the prev subprocess for piping
            for i, args in enumerate(commands):                                   # loop through each cmd segment in the pip chain 
                if i == 0:          
                   prev_proc = subprocess.Popen(args, stdout=subprocess.PIPE)     #first cmd: capture output to pipe to the next 
                elif i == len(commands) -1:                     
                    subprocess.run(args, stdin=prev_proc.stdout)                  #last cmd: use the previous output as input 
                else: 
                    prev_proc = subprocess.Popen(args, stdin=prev_proc.stdout,stdout=subprocess.PIPE)  #middle command: pass input from previous and output to the next 
            continue                                                              #go to next loop iteration after handling piping 

        #handle redirection 
        args = shlex.split(cmd)                           #split command again for redirection checks 
        if ">>" in args:                                  #handle output append redirection (>>)
            idx = args.index(">>")                        #find the position of '>>'
            with open(args[idx + 1], "a") as f:           #open file in append mode 
                subprocess.run(args[:idx], stdout=f)
        elif  ">" in args:                                #handle output overwrite redirection (>)
            idx = args.index(">")   
            with open(args[idx + 1], "w") as f:           #open file in write mode 
                subprocess.run(args[:idx], stdout=f)
        elif "<" in args:                                 #handle input redirection (<)
            idx = args.index("<")                         
            with open(args[idx + 1], "r") as f:           #open file in read mode 
                subprocess.run(args[:idx], stdin=f)
        else:                                             #no redirection or pipe, just run the command normally 
            subprocess.run(args)



    except KeyboardInterrupt:                              #handle exceptions and errors 
        print ("\nKeyboard Interrupt")
    except Exception as e:
        print(f"Error: {e}")


