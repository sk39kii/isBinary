# isBinary
Pythonでバイナリ判定

## 概要
簡易バイナリ判定を行います。  
※2016-09-24追記 レポジトリを新しく切り直しました。

## 使い方

### コマンド

```py
python isBinary.py [TargetFile]
```

## 判定内容
MIMEタイプを取得して判断します。
* imageやofficeの場合はTrue(=Binary)。   
* textやcsv(application/vnd.ms-excel)の場合はFalse(=Not Binary)  

MIMEが取得できない場合(L21〜L37)は以下で判定してます。
(使うシーンに合わせて変えてください)  
* ファイルの中身でエンコードが取得しエンコードが不明の場合はBinary
* ファイルの中身にASCIIコードの00H-08Hの文字があればBinary

※エンコードのconfidence（信頼性）の値はとくに見てません

### 実行例

README.mdファイルをチェックします。

```sh
$ python isBinary.py  README.md 
README.md is Binary? : False
``` 

画像ファイルをチェックします。

```sh
$ python isBinary.py sample.png 
sample.png is Binary? : True
```
