from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        shlvl = os.environ.get("SHLVL")
        if shlvl:
            self.powerline.append(" %s " % os.path.basename(shlvl),
                                    self.powerline.theme.SSH_FG,
                                    self.powerline.theme.SSH_BG)
