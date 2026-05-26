run.py: 运行
main.py: 测试连接Linux和获取命令返回值字段
homepage.py: 主界面内容



在VMware中的虚拟机中安装ssh服务
sudo apt-get update
sudo apt-get install openssh-client
sudo apt-get install openssh-server
sudo service ssh start
经过上面几步之后，SSH已经基本安装成功，现在查看是否安装成功：
sudo ps -e | grep ssh



配置免密登录
第一步：在windows命令行（python终端也可以）中输入ssh-keygen -t rsa
第二步：把生成的公钥id_rsa.pub复制到服务器上可以手动
（需要把.ssh文件权限改为700，id_rsa.pub文件改为600）
推荐使用命令ssh-copy-id zhang@192.168.154.128
如果没有提示你没有改命令可以git命令行
第三步：测试是否配好在命令行中输入ssh 用户@ip

shell脚本编写
打开终端输入nano top_script.sh（你也可以使用其他文本编辑器）
编辑top -b -n 1
保存退出就可以了

修改ip
查看Ubuntu的ip地址：ifconfig
修改home.py中的ip等
