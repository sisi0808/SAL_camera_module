import paramiko
import scp as scp

#ここでは自前のラズパイでテスト
hostname = '192.168.13.30'
port = 57532
username = 'pisa'
password = 'test_pass_8/7'

#画像の転送
def send(path):
    #sshを用いて親機へファイルを転送
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        with scp.SCPClient(ssh.get_transport()) as scp2:
            scp2.put(path,'/home/pisa/img')
    print("rest")

if __name__ == '__main__':
  print("import only")