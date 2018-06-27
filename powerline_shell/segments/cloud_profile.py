from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        cloud_profile = os.environ.get("profile_name") or \
            os.environ.get("AWS_DEFAULT_PROFILE")
        if cloud_profile:
            self.powerline.append(" %s " % os.path.basename(cloud_profile),
                                    self.powerline.theme.CLOUD_PROFILE_FG,
                                    self.powerline.theme.CLOUD_PROFILE_BG)
