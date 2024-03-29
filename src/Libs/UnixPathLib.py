#!UnixPathLib <Dependency which contains functions to validate the paths in the change directory command for unix>


def isabsolute(path,user):
    #Check whether the path is absolute or not

    if(len(remover(splitdirectory(path)))!=0):
        if(path[0]=="/" or remover(splitdirectory(path))[0]=="~" or remover(splitdirectory(path))[0].upper()=="$HOME"or (remover(splitdirectory(path))[0]=="/" and remover(splitdirectory(path))[1]=="home" and remover(splitdirectory(path))[2]==user)):
            return True
        else:
            return False
    else:
        return False

def remover(directories):

    #Remove the empty quotes
    while ('' in directories):
        directories.remove('')
    return directories

def splitdirectory(path):
    #spearate each and every directories from path
    
    if (path!=""):
        directories=path.split("/")
        if path[0]=="/":
            directories.insert(0,"/")
        return directories
    else:
        return list()



def JoinrootPath(Directories):
    #Join the Directories with slash
    path=""
    for directory in Directories:
        if directory=="/":
            path+='/'
        else:
            path+=directory+"/"
    return path

def CountDirectories(path):

    #Count the number of directories in the path <Count from the root directory> 
    count=0
    directories=remover(splitdirectory(path))

    for directory in directories:
        count+=1
    return count


def BackDir(user,cwd,path):
    #Used to return to parent directories
    root="/"
    if (not isabsolute(path,user)):
        cwd=remover(splitdirectory(cwd));cwd.pop(0)   #Relative path navigation
        path=remover(splitdirectory(path))
    else:
        cwd=remover(splitdirectory(cwd))
        path=remover(splitdirectory(path))      #Absolute path navigation
        cwd.clear()
        
    for directory in path:
        if (directory==".." and len(cwd)!=0):
            cwd.pop()
        elif (directory!=".."):
            cwd.append(directory)

    cwd.insert(0,root)
    return JoinrootPath(cwd)
    
    

        

def BackDotRemover(cmd):

    #Return the List of Corrected Command
    NewDirectories=list()
    for directory in cmd:
        if (directory.count('.')==len(directory) and directory.count('.')==1):
            pass
        else:
            NewDirectories.append(directory)
    return NewDirectories


def isBack(path):

    #Return true the path contains back navigation
    path=remover(splitdirectory(path))
    if ".." in path:
        return True
    else:
        return False


def replacer(path,user):
    #Reverse the home path with tidle sign
    directories=remover(splitdirectory(path))

    if (isabsolute(path,user) and CountDirectories(path)>=3):
        if (directories[0]=="/" and directories[1]=="home" and directories[2]==user):
            directories.pop(0);directories.pop(0);directories.pop(0);directories.insert(0,"~")

        elif (directories[0].upper()=="$HOME"):
            directories.pop(0);directories.insert(0,"~")
    return JoinrootPath(directories)
            
    
def ReverseReplacer(path,user):
    #Reverse the tidle sign with home path 
    directories=remover(splitdirectory(path))

    if isabsolute(path,user):
        if (directories[0]=="~"or directories[0].upper()=="$HOME"):
            directories.pop(0);directories.insert(0,"/");directories.insert(1,"home");directories.insert(2,user)

    return JoinrootPath(directories)
    
