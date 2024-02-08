import requests

def get_versions() -> list[str]:
    """Get all minecraft versions.

    Returns:
        list[str]: Sorted list of every minecraft version.
    """

    data = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json", headers={"Accept": "application/json"})
    data = data.json()
    versions = []
    
    for version in data["versions"]:
        if version["type"] == "release":
            versions.append(version["id"])
    
    return versions