def download(type: str, version: str, url: str):
    import Storage
    Storage.logger.debug(f'Downloading {type} version {version} from {url}')
    import os
    if not os.path.isfile(f'jar/stable/{type}/{type}-{version}.jar'):
        Storage.logger.info(f'Downloading {type} ({version})')
        import requests
        r = requests.get(url, allow_redirects=True)
        open(f'jar/stable/{type}/{type}-{version}.jar', 'wb').write(r.content)
        Storage.logger.info(f'Downloaded {type} ({version}) to jar/stable/{type}/{type}-{version}.jar')
    else:
        Storage.logger.info(f'{type}-{version}.jar already exists on disk, skipping download')
