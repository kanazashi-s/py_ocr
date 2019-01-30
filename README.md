py_ocr
====

画像ファイルの中にある文字を抽出します。OCRです。  
TesseractというオープンソースのOCRソフトウェアと、それをPython上で使えるようラップするライブラリ、pyocrを用いました。  

## Demo
画像ファイルを読み込み文字認識を行っています。  
文字認識を行う際に画像上の座標もともに取得し、出力場所を合わせています。  
![TestPngImg](https://github.com/zashio/py_ocr/blob/master/tesseracttest.png)

今回は手書き文字認識については行っておりません。

## Usage
### Tesseractのインストール
まずはTesseractをインストールしてください。  
ここでインストールしたTesseractを、pyocrでラップして利用します。  

[インストール方法](https://github.com/tesseract-ocr/tesseract/wiki)  
日本語版は[このあたり](https://www.kunihikokaneko.com/dblab/licenseplate/tesseract.html)が参考になるでしょう。  
  
### ソースコードのコピー
- コンソールを開き、任意の場所で以下を実行し、全てのファイルをダウンロードしてください。  
`git clone https://github.com/zashio/py_ocr.git`  
- py_ocrフォルダ内に移動し、コンソール上で以下を実行し、必要なライブラリをインストールしてください。  
`pip install -r requirements.txt`   

