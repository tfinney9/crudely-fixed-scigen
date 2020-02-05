#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:00:50 2020

@author: tfinney
"""

import os
import subprocess
import glob


class scigen():
    def __init__(self,out_dir,auto_run=True):
        self.base_dir = '/home/tfinney/src/scigen/'
        self.out_dir = self.base_dir+out_dir
        
        if(auto_run==True):
            os.chdir(self.base_dir)
            self.check_out_dir(self.out_dir)
            self.gen_scigen(self.out_dir)
            os.chdir(self.out_dir)
            self.comp_latex(self.out_dir)
    
    def check_out_dir(self,out):
        if(os.path.exists(out)==False):
            print("making out directory",out)
            os.mkdir(out)
    
    
    def gen_scigen(self,save_dir):
        """
        Need to Add authors
        """
        header = "#!/bin/bash"
        front_matter = "export PERL5LIB=/home/$USER/src/scigen"
        scigen_command = "./make-latex.pl --savedir " + save_dir
        list_cmds = [header,front_matter,scigen_command]
        
        content = '\n'.join(list_cmds)
        
        with open('run_scigen.sh','w') as f:
            f.write(content)
            f.close()
        
        subprocess.check_output(['sh','run_scigen.sh'])
    
    
    def comp_latex(self,out):
        tex_file = glob.glob(out+"*.tex")[0]
        tt = os.path.basename(tex_file) #placeholder to strip away abs path
        bib_file = tt[:-4]
        
        tex_cmd = 'pdflatex '+tex_file
        bib_cmd = 'bibtex '+bib_file
        
        tex_list = [tex_cmd,bib_cmd,tex_cmd,tex_cmd]
        tex_cont = '\n'.join(tex_list)
    
        with open(out+"comp_latex.sh",'w') as f:
            f.write(tex_cont)
            f.close()
            
        # os.chdir(out)
        pipes = subprocess.Popen(['sh','comp_latex.sh'],stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        std_out,std_err = pipes.communicate()    
        
     
        
x = scigen('out5/')