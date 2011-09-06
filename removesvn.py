#! /usr/bin/env python

import os
import sys
import shutil

class SVNRemover(object):
    
    def __init__(self):
        """Constructor"""
        try:
            self.path = sys.argv[1]
        except IndexError:
            print 'The first argument needs to be the path. None is given.'
            exit()
            
        if not os.path.exists(self.path):
            print 'The given path does not exist'
            exit()
        
        # Remove slash at the end of the path
        if self.path[len(self.path) - 1] == '/':
            self.path = self.path[0:(len(self.path) - 1)]
        
        self.count = 0
        
    def remove_svn(self, path):
        """Runs recursively through the given path and removes all .SVN folders"""
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