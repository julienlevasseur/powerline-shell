from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        cloud_profile = os.environ.get("profile_name") or \
            os.environ.get("AWS_DEFAULT_PROFILE")
        if cloud_profile:
            fg = self.powerline.theme.CLOUD_PROFILE_FG
            bg = self.powerline.theme.CLOUD_PROFILE_BG
            profile = os.path.basename(cloud_profile)
            self.powerline.append(" %s " % profile, fg, bg)
