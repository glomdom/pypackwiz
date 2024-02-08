import os

class Pack:
    """Contains generic information about a pack - name, author, minecraft version, pack version, modloader version, etc."""

    def __init__(self, name, author, mc_version, pack_version, modloader, modloader_version):
        self.name = name
        self.author = author
        self.mc_version = mc_version
        self.pack_version = pack_version
        self.modloader = modloader
        self.modloader_version = modloader_version
    
    def initialize(self, directory):
        """Initializes the pack with packwiz. All metadata from constructor must be set to a valid value."""

        prev_dir = os.curdir
        os.chdir(directory)

        print(prev_dir, directory)

        os.chdir(prev_dir)

    def pack_meta(self):
        """Returns the pack metadata in the following order:
        
        pack_name, author, pack_version, mc_version, modloader, modloader_version
        """

        return self.name, self.author, self.pack_version, self.mc_version, self.modloader, self.modloader_version