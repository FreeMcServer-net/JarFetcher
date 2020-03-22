def generate(type: str, version: str, stage: str):
    import Storage
    import os
    if type is 'custom':
        return
    stage_label = ''
    if stage == 'snapshot':
        stage_label = '-snapshot'
    if not os.path.exists(f'conf-template/{stage}/{type}/{type}.template'):
        Storage.logger.error(f'conf-template/{stage}/{type}/{type}.template dosent exist, config will not be generate')
        return
    Storage.logger.debug(f'Generating config for {stage} {type} version {version}')
    Storage.logger.info(f'{stage} - Generating {type} ({version})')
    with open(f'conf-template/{stage}/{type}/{type}.template', 'r') as file:
        template = file.read()
        template = template.replace('[TYPE]', type).replace('[VERSION]', version)
        if os.path.exists(f'conf/{stage}/{type}/{type}-{version}{stage_label}.jar.conf'):
            Storage.logger.info(f'Config conf/{stage}/{type}/{type}-{version}{stage_label}.jar.conf exists, will '
                                f're-create')
            os.remove(f'conf/{stage}/{type}/{type}-{version}{stage_label}.jar.conf')
            Storage.logger.debug(f'caralho {stage}')
            Storage.logger.debug(f'caralho {stage_label}')
        with open(f'conf/{stage}/{type}/{type}-{version}{stage_label}.jar.conf', 'a') as output_file:
            output_file.write(template)
            Storage.logger.info(f'Config conf/{stage}/{type}/{type}-{version}{stage_label}.jar.conf generated')
