#! /usr/bin/env python

import os
import sys
import shutil

class SVNRemover(object):
    
    def __init__(self):
        arguments = sys.argv
        self.path = arguments[1]
        self.count = 0
        pass
        
    def remove_svn(self, path):
        """Runs recursively through the given path and removes all .SVN folders"""
        # What if slash at the end of path? remove it
        if os.path.exists(path) and os.path.isdir(path):
            directory_listing = os.listdir(path)
            for folder in directory_listing:
                if folder == ".svn":
                    file = path + "/.svn"
                    print "Removing SVN folder " + file
                    self.count = self.count + 1
                    shutil.rmtree(file)
                
                new_path = path + "/" + folder
                self.remove_svn(new_path)

    def run(self):
        """Run the script"""
        self.remove_svn(self.path)
        if self.count == 0:
            print "No SVN folders have been found"
        
remover = SVNRemover()
remover.run()