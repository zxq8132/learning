折腾几次终于用git将文件传到了github上了。
步骤：
1、echo "# my_page" >> README.md
2、git init
3、git add README.md
4、git commit -m "first commit"
5、git remote add origin git@github.com:myuser/my_page.git#这个在新建仓库的时候就有呀
6、git push -u origin master
坑：
1、win10要用使用的是Git下要用使用的是Git CMD工具呀！如果用Git Bash，各种无语呀，百度出来的教程坑太大。

