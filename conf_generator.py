def generate(type: str, version: str, stage: str):
    import Storage
    import os
    if type is 'custom':
        return
    if not os.path.exists(f'conf-template/{stage}/{type}/{type}.template'):
        Storage.logger.error(f'conf-template/{stage}/{type}/{type}.template dosent exist, config will not be generate')
        return
    Storage.logger.debug(f'Generating config for {stage} {type} version {version}')
    Storage.logger.info(f'{stage} - Generating {type} ({version})')
    with open(f'conf-template/{stage}/{type}/{type}.template', 'r') as file:
        template = file.read()
        template = template.replace('[TYPE]', type).replace('[VERSION]', version)
        if os.path.exists(f'conf/{stage}/{type}/{type}-{version}.jar.conf'):
            Storage.logger.info(f'Config conf/{stage}/{type}/{type}-{version}.jar.conf exists, will re-create')
            os.remove(f'conf/{stage}/{type}/{type}-{version}.jar.conf')
        with open(f'conf/{stage}/{type}/{type}-{version}.jar.conf', 'a') as output_file:
            output_file.write(template)
            Storage.logger.info(f'Config conf/{stage}/{type}/{type}-{version}.jar.conf generated')
