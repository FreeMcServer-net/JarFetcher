import concurrent.futures
import os
import shutil
from zipfile import ZipFile

import Storage
import conf_generator
import downloader
import import_generator
from link_providers import CraftBukkitProvider, SpigotProvider, VanillaProvider

all_links = {
    'craftbukkit': {},
    'nukkit': {},
    'paper': {},
    'spigot': {},
    'vanila': {},
}

Storage.init_logger()
Storage.logger.info('JarFetcher starting')
Storage.logger.info('Getting CraftBukkit links')
# Using hardcoded values for easier dev
all_links['craftbukkit'].update(CraftBukkitProvider.get())
all_links['spigot'].update(SpigotProvider.get())
all_links['vanila'].update(VanillaProvider.get())
all_paths = []

Storage.logger.debug(all_links)
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = []
    for jar_type in all_links:
        Storage.logger.info(f'Downloading {jar_type} jars')
        for jar_name in all_links[jar_type]:
            jar_link = all_links[jar_type][jar_name]
            jar_version = jar_name.split('-')[1].replace('.jar', '')
            Storage.logger.debug(f'{jar_name} ({jar_version}): {jar_link}')
            results.append(executor.submit(downloader.download, jar_type, jar_version, jar_link))
Storage.logger.info('Generating configs')
for stage in os.listdir('jar'):
    for jar_type in os.listdir(f'jar/{stage}'):
        Storage.logger.info(f'Generating configs for {stage} -> {jar_type}')
        for jar_name in os.listdir(f'jar/{stage}/{jar_type}'):
            if jar_name.startswith('.') or os.path.isdir(f'jar/{stage}/{jar_type}/{jar_name}'):
                continue
            Storage.logger.info(f'Generating configs for {jar_name}')
            jar_version = jar_name.split('-')[1].replace('.jar', '')
            conf_generator.generate(jar_type, jar_version, stage)

Storage.logger.info('Generating import')
import_command = ''
for stage in os.listdir('jar'):
    for jar_type in os.listdir(f'jar/{stage}'):
        Storage.logger.info(f'Generating configs for {stage} -> {jar_type}')
        for jar_name in os.listdir(f'jar/{stage}/{jar_type}'):
            if jar_name.startswith('.') or os.path.isdir(f'jar/{stage}/{jar_type}/{jar_name}'):
                continue
            # all_paths.append(f'jar/{stage}/{jar_type}/{jar_name}')
            all_paths.append(f'conf/{stage}/{jar_type}/{jar_name}.conf')
            Storage.logger.info(f'Generating configs for {jar_name}')
            jar_version = jar_name.split('-')[1].replace('.jar', '')
            import_command += import_generator.generate(jar_type, jar_version, stage)
shutil.copy('conf-template/stable/custom/custom.template', 'conf/stable/custom/custom.jar.conf')
all_paths.append('conf/stable/custom/custom.jar.conf')
if os.path.exists('import.sql'):
    os.remove('import.sql')

with open(f'import.sql', 'a') as output_file:
    output_file.write(import_command)
    Storage.logger.info('Saved import.sql file')

print(all_paths)

if os.path.exists('zip/dist.zip'):
    os.remove('zip/dist.zip')
with ZipFile('zip/dist.zip', 'w') as zip:
    for file in all_paths:
        zip.write(file, os.path.basename(file))
