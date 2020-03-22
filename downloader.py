def download(type: str, version: str, url: str, stage: str):
    import Storage
    Storage.logger.debug(f'Downloading {type} version {version} from {url}')
    import os
    stage_label = ''
    if stage == 'snapshot':
        stage_label = '-snapshot'
    if not os.path.isfile(f'jar/{stage}/{type}/{type}-{version}{stage_label}.jar'):
        Storage.logger.info(f'Downloading {type} ({version})')
        import requests
        r = requests.get(url, allow_redirects=True)
        open(f'jar/{stage}/{type}/{type}-{version}{stage_label}.jar', 'wb').write(r.content)
        Storage.logger.info(f'Downloaded {type} ({version}) to jar/{stage}/{type}/{type}-{version}{stage_label}.jar')
        Storage.new_installs.append(
            f"http://jar.freemcserver.net/conf/{stage}/{type}/{type}-{version}{stage_label}.jar.conf")
    else:
        Storage.logger.info(f'{stage}-{type}-{version}{stage_label}.jar already exists on disk, skipping download')
