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
    'stable': {
        'craftbukkit': {},
    'nukkit': {},
    'paper': {},
    'spigot': {},
    'vanila': {},
    },
    'snapshot': {
        'craftbukkit': {},
        'nukkit': {},
        'paper': {},
        'spigot': {},
        'vanila': {},
    },

}

Storage.init_logger()
Storage.logger.info('JarFetcher starting')
Storage.logger.info('Getting CraftBukkit links')
# Using hardcoded values for easier dev
all_links['stable']['craftbukkit'].update(CraftBukkitProvider.get())
all_links['stable']['spigot'].update(SpigotProvider.get())
all_links['stable']['vanila'].update(VanillaProvider.get())
# all_links['snapshot']['vanila'].update(VanillaSnapshotProvider.get())
all_paths = []

Storage.logger.debug(all_links)
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = []
    for stage in all_links:
        for jar_type in all_links[stage]:
            Storage.logger.info(f'Downloading {jar_type} jars')
            for jar_name in all_links[stage][jar_type]:
                jar_link = all_links[stage][jar_type][jar_name]
                jar_version = jar_name.split('-')[1].replace('.jar', '')
                Storage.logger.debug(f'{jar_name} ({jar_version}): {jar_link}')
                results.append(executor.submit(downloader.download, jar_type, jar_version, jar_link, stage))
Storage.logger.info('Generating configs')
for stage in os.listdir('jar'):
    for jar_type in os.listdir(f'jar/{stage}'):
        Storage.logger.info(f'Generating configs for {stage} -> {jar_type}')
        for jar_name in os.listdir(f'jar/{stage}/{jar_type}'):
            if jar_name.startswith('.') or os.path.isdir(f'jar/{stage}/{jar_type}/{jar_name}'):
                continue
            Storage.logger.info(f'Generating configs for {jar_name}')
            jar_version = jar_name.split('-')[1].replace('.jar', '').replace('-snapshot', '')
            conf_generator.generate(jar_type, jar_version, stage)

Storage.logger.info('Generating import')
import_command = ''
for stage in os.listdir('jar'):
    for jar_type in os.listdir(f'jar/{stage}'):
        Storage.logger.info(f'Generating configs for {stage} -> {jar_type}')
        import_command += f'# ------- START {stage} {jar_type} -------\n'
        for jar_name in os.listdir(f'jar/{stage}/{jar_type}'):
            if jar_name.startswith('.') or os.path.isdir(f'jar/{stage}/{jar_type}/{jar_name}'):
                continue
            all_paths.append(f'jar/{stage}/{jar_type}/{jar_name}')
            all_paths.append(f'conf/{stage}/{jar_type}/{jar_name}.conf')
            Storage.logger.info(f'Generating configs for {jar_name}')
            jar_version = jar_name.split('-')[1].replace('.jar', '')
            import_command += import_generator.generate(jar_type, jar_version, stage)
        import_command += f'# ------- FINISH {stage} {jar_type} -------\n'
shutil.copy('conf-template/stable/custom/custom.template', 'conf/stable/custom/custom.jar.conf')
all_paths.append('conf/stable/custom/custom.jar.conf')
if os.path.exists('import.sql'):
    os.remove('import.sql')

if os.path.exists('install.txt'):
    os.remove('install.txt')

with open(f'install.txt', 'a') as output_file:
    for link in Storage.new_installs:
        output_file.write(f'{link} \n')
    Storage.logger.info('Saved install file')


with open(f'import.sql', 'a') as output_file:
    output_file.write(import_command)
    Storage.logger.info('Saved import.sql file')

if os.path.exists('zip/dist.zip'):
    os.remove('zip/dist.zip')
with ZipFile('zip/dist.zip', 'w') as zip:
    for file in all_paths:
        zip.write(file, os.path.basename(file))
