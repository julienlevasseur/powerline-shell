from ..utils import BasicSegment
import os

from python_terraform import *

def in_initialized_terraform_folder():
    if os.path.exists("./.terraform"):
        return True 
    else:
        return False

def get_wokspace_name():
    t = Terraform()
    return_code, stdout, sterr = t.cmd('workspace', 'list')
    for workspace in stdout.split('\n'):
        if "*" in workspace:
            return workspace.split('* ')[1]

class Segment(BasicSegment):
    def add_to_powerline(self):
        if in_initialized_terraform_folder():
            fg = self.powerline.theme.TF_WORKSPACE_FG
            bg = self.powerline.theme.TF_WORKSPACE_BG
            workspace = get_wokspace_name()
            self.powerline.append(" %s " % workspace, fg, bg)
