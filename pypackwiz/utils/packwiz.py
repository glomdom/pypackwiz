import shutil
import subprocess
import os
import requests
import platform

from pathlib import Path
from . import logger
from . import colors

# License permits redistribution.
WINDOWS_LINK = "https://file.garden/ZcScYBFyZHPCTo1X/windows_packwiz/packwiz.exe"
LINUX_LINK = "https://file.garden/ZcScYBFyZHPCTo1X/linux_packwiz/packwiz"
MAC_LINK = "https://file.garden/ZcScYBFyZHPCTo1X/mac_packwiz/packwiz"

class Packwiz:
    def __init__(self, pack_dir):
        self.pack_dir = Path(pack_dir)
        self.pypackwiz_dir = self.pack_dir / ".pypackwiz/"
        self.pypackwiz_bin_dir = self.pypackwiz_dir / "bin/"
        self.packwiz_exec = None
    
    def create_directory_structure(self) -> None:
        prev_dir = os.curdir

        os.makedirs(self.pypackwiz_bin_dir, exist_ok=True)
        os.chdir(prev_dir)

    def create_git_repository(self) -> bool:
        git_exec = shutil.which("gitter")

        if not git_exec:
            logger.warn("git command not found. skipping repository creation.")
            
            return False
        
        logger.info("creating git repository..", end="\r")
        subprocess.Popen([git_exec, "init", self.pack_dir])
        logger.info("creating git repository.. {}ok".format(colors.GREEN))

        return True

    def pack_name_from_dir(self) -> str:
        pack_dir_str = str(self.pack_dir)
        pack_dir_str.replace("-", " ").replace("_", " ").title()

        return pack_dir_str

    def download_packwiz(self) -> None:
        url = ""
        out_file = ""

        match platform.system():
            case "Windows": url = WINDOWS_LINK
            case "Linux": url = LINUX_LINK
            case "Mac": url = MAC_LINK
            case _: logger.error("unsupported platform {}".format(platform.system()))

        out_file = self.pypackwiz_bin_dir / url.split('/')[-1]

        with requests.get(url) as r:
            r.raise_for_status()

            with open(out_file, "wb") as f:
                f.write(r.content) # Redundant to stream as file is 10MB.
        
        self.packwiz_exec = out_file.absolute()
