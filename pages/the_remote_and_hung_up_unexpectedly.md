title:  heroku does not appear to be a git repositoryの対処方法
date: 2013-09-24
tags: heroku

既存のherokuでデプロイしたアプリを別環境で動かそうとしたら、herokuというレポジトリはないというエラーが出た。

git remote add で登録すればokだった。

    git remote add heroku git@heroku.com:{my-project-name}.git






