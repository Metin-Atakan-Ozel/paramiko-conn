
from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()

#client.load_host_keys('C:\\Users\\metin/.ssh/id_rsa')
#client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("192.168.1.30",username='root', password="---", timeout=15)

#stdin,stdout,stderr = client.exec_command("ifconfig")
#stdin,stdout,stderr = client.exec_command("reboot")
stdin,stdout,stderr = client.exec_command("systemctl restart NetworkManager",timeout=5)
#stdin,stdout,stderr = client.exec_command("ifconfig enp0s3 192.168.1.33")


print(f'STDOUT:{stdout.read().decode("utf-8")}')
print(f'STDOUT:{stderr.read().decode("utf-8")}')

stdin.close()
stdout.close()
stderr.close()
client.close()
