jar_types = {
    'stable': {
        'craftbukkit': 3,
        'nukkit': 5,
        'paper': 4,
        'spigot': 1,
        'vanila': 2,
    },
    'snapshot': {
        'craftbukkit': 6,
        'nukkit': None,
        'paper': None,
        'spigot': 7,
        'vanila': 10,
    }
}


def generate(type: str, version: str, stage: str):
    stage_label = ''
    if stage is 'snapshot':
        stage_label = '-snapshot'
    command = f"INSERT IGNORE INTO `jars` (`id`, `id_type`, `internal_name`, `version`,  `active`, `default`) VALUES (NULL, {jar_types[stage][type]}, '{type}-{version}{stage_label}.jar', '{version}',  '0', '0');\n"
    return command
