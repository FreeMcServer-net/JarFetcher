import os

os.system("rm -rf downloads/dist/*.jar")
os.system("rm -rf downloads/dist/*.jar.conf")
os.system("rm -rf downloads/dist/*.zip")
os.system("/usr/bin/find downloads/jar -iname '*.jar' -exec cp --target-directory downloads/dist {} \;")
os.system("/usr/bin/find downloads/conf -iname '*.jar.conf' -exec cp --target-directory downloads/dist {} \;")
with open('templates/stable/custom.template', 'r') as file:
    template = file.read()
    if os.path.exists('downloads/dist/custom.jar.conf'):
        os.remove('downloads/dist/custom.jar.conf')
    with open('downloads/dist/custom.jar.conf', 'a') as the_file:
        the_file.write(template)
os.system("cd downloads/dist && /usr/bin/zip -R -D dist.zip *")
os.system("rm -rf /var/www/html/*")
os.system("cp -R downloads/* /var/www/html")
