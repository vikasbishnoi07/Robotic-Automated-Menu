def hadoopsetmaster():
        import os
        os.system("ansible-playbook copy.yml")
        os.system('ansible master -m command -a "rpm -ivh jdk-8u171-linux-x64.rpm --force"')
        os.system('ansible master -m command -a "echo export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/ >> /root/.bashrc"')
        os.system('ansible master -m command -a "echo export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH >>/root/.bashrc"')	
        os.system('ansible master -m command -a "rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"')
        os.system('ansible master -m command -a "hostnamectl set-hostname master.avn"')
        os.system('ansible-playbook master.yml')
def hadoopsetslave():
        import os
        os.system("ansible-playbook copy.yml")
        os.system('ansible slave -m command -a "rpm -ivh jdk-8u171-linux-x64.rpm --force"')
        os.system('ansible slave -m command -a "JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/"')
        os.system('ansible slave -m command -a "PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH"')
        os.system('ansible slave -m command -a "echo export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/ >> /root/.bashrc"')
        os.system('ansible slave -m command -a "echo export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH >>/root/.bashrc"')	
        os.system('ansible slave -m command -a "rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"')
        os.system('ansible-playbook slave.yml')
def hadooprunmaster():
        import os
        os.system('ansible master -m command -a "hadoop namenode -format"')
        os.system('ansible master -m command -a " hadoop-daemon.sh start namenode"')
def hadooprunslave():
        import os
        os.system('ansible slave -m command -a " hadoop-daemon.sh start datanode"')
def hadoopsetjt():
        import os
        os.system('ansible master -m command -a "hostnamectl set-hostname jobtracker.avn"')
        os.system('ansible-playbook jt.yml')
def hadoopsettt():
        import os
        os.system('ansible-playbook tt.yml')
def hadooprunjt():
        import os
        os.system('ansible slave -m command -a " hadoop-daemon.sh start jobtracker"')
def hadoopruntt():
        import os
        os.system('ansible slave -m command -a " hadoop-daemon.sh start tasktracker"')
