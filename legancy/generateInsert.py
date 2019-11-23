import os
insert = ""
for filename in os.listdir("downloads/dist"):
    if not filename.endswith(".jar"):
        continue
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    stability = "stable"
    stabilityLabel = ""
    if "snapshot" in filename:
        stability = "snapshot"
        stabilityLabel = "-snapshot"
    if type == "spigot":
        c = 1
        if stability == 'snapshot':
            c = 7
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `id_type`, `internal_name`, `version`,  `active`, `default`) VALUES (NULL, %s, 'spigot-%s%s.jar', '%s',  '0', '0');\n" % (
            c, version, stabilityLabel, version)
    if type == "vanilla":
        c = 2
        if stability == 'snapshot':
            c = 10
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `id_type`, `internal_name`, `version`,  `active`, `default`) VALUES (NULL, %s, 'vanilla-%s%s.jar', '%s',  '0', '0');\n" % (
        c, version, stabilityLabel, version)
    if type == "paperspigot":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `id_type`, `internal_name`, `version`,  `active`, `default`) VALUES (NULL, 4, 'paperspigot-%s%s.jar', '%s',  '0', '0');\n" % (
        version, stabilityLabel, version)

    if type == "nukkit":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `id_type`, `internal_name`, `version`,  `active`, `default`) VALUES (NULL, 5, 'nukkit-%s%s.jar', '%s',  '0', '0');\n" % (
        version, stabilityLabel, version)

if os.path.exists('import.sql'):
    os.remove('import.sql')
with open('import.sql', 'a') as the_file:
    the_file.write(insert)