from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        shlvl = os.environ.get("SHLVL")
        fg = self.powerline.theme.SSH_FG
        bg = self.powerline.theme.SSH_BG
        if shlvl:
            self.powerline.append(" %s " % os.path.basename(shlvl), fg, bg)
