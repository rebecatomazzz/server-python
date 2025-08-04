import subprocess
import os
import sys
import shutil
#verifica super usur
def is_superuser():
return os.geteuid() == 0
if not is_superuser():
print("esse script precisa de super user")
sys.exit(1)
caminho_projeto = "/var/www/html/projeto-1"
arquivos_copia = ['css', 'img', 'index.html', 'README.md']
for file in arquivos_copia:
src_caminho = os.path.join(caminho_projeto, file)
dest_caminho = '/var/www/html'
    if os.path.exists(src_caminho):
            print("copiando {file} para {dest_caminho}")
            if os.path.isdir(src_caminho):
                    shutil.copytree(src_caminho, os.path.join(dest_caminho, file), dirs_exists_ok=True)
    else
                    shutil.copy(src_caminho, dest_caminho)
if not os.path.exists("/etc/apache2"):
print("Apache nao esta intalando")
subprocess.call(["apt-get", "update", "apache2", "-y"])
print("inicioando o servidor")
subprocess.call(["systemctl", "start", "apache2"])
print("inicioando o status")
subprocess.call(["systemctl", "status", "apache2"])
