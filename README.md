# Robosys2
ロボットシステム学＿課題２
---
## 概要
ロボットシステム学の課題2として作成しました。
センサの前に物を置くと、サーボモータが大吉・中吉・吉・小吉・凶のうちのどれかをランダムで指し、置いた物のその年の運勢をおみくじで占います。

---
## 使用用途
本ドライバは複数の他マイコンボードに同時に信号を送ることができるため、複数のマイコンボードを同時に操作したり、Raspberry Pi4だけではピンが足りない場合に他のマイコンボードを使用しピン数を拡張することができます。

---
## 動画
- 画像をクリックするとYoutubeで動画が再生されます
[![動画](https://user-images.githubusercontent.com/71487860/148649143-e5f5aa0b-eec9-4b44-a214-d88428af4b0a.png)](https://youtu.be/1IIlWhmQFRc)


---
## 使用物品
|No.|物品名|数量|
|---|---|---|
|1|Raspberry Pi4 ModelB / 8GB|1|
|2|ブレッドボード|4|
|3|ジャンパ線|24|
|4|ラズベリーパイＢ＋／Ａ＋用ブレッドボード接続キット|1|
|5|抵抗器(48Ω)|1|
|6|抵抗器(100KΩ)|1|
|7|LBR-127hld|1|
|8|抵抗内蔵LED(青)|4|
|9|抵抗内蔵LED(赤)|4|
|10|抵抗内蔵LED(緑)|5|

---
## 回路
- 回路図
[回路図](https://github.com/YukiShigematsu/Robosys2/files/7833501/ROS.pdf)
<img src="https://user-images.githubusercontent.com/71487860/148650694-9c5a18fd-c29c-4a38-b6f6-0b9d4397e021.png" width="1280px">

- 実配線
<img src="https://user-images.githubusercontent.com/71487860/148650820-e9098a99-32ce-4ced-8afa-ac8549ccff96.jpg" width="640px">

#### 使用するGPIOピンと用途
- Raspberry Pi4 ModelB / 8GB

|NO.|GPIOピン|用途|
|---|---|---|
|1|+５V|サーボモータとLBR-127hldへの5V供給|
|2|GND|各LED,サーボモータ、LBR-127hldへのGND電圧供給|
|3|GPIO3|LEDのアノードへ電圧供給|
|4|GPIO5|LEDのアノードへ電圧供給|
|5|GPIO9|LEDのアノードへ電圧供給|
|6|GPIO10|LEDのアノードへ電圧供給|
|7|GPIO11|LBR-127hldからの信号入力|
|8|GPIO17|LEDのアノードへ電圧供給|
|9|GPIO18|サーボモータへPWM信号出力|
|10|GPIO22|LEDのアノードへ電圧供給|
|11|GPIO27|LEDのアノードへ電圧供給|

---

## ROS環境構築(ROS1)

ROSの環境構築は下記のスクリプトを使用し行いました。
[ros_setup_scripts_Ubuntu20.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)

## ワークスペース作成

ワークスペースの作成は下記の資料を参考に作成しました。
[robosys2020 ros.md](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)

---

## パッケージ実行方法
1. #### 以下のコマンドを実行してパッケージをクローン

~~~
`$ cd ~/catkin_ws/src
`$ git clone https://github.com/YukiShigematsu/Robosys2.git
~~~

`$ echo f > /dev/signal0`
- NUCLEO-F446REに接続されているLEDが流れるように点滅する信号を送信します

2. #### cross

`$ echo c > /dev/signal0`
- NUCLEO-F446REに接続されているLEDが交わるように点滅する信号を送信します

3. #### together

`$ echo t > /dev/signal0`
- NUCLEO-F446REに接続されているLEDが3つずつ点滅する信号を送信します

4. #### blinking

`$ echo b > /dev/signal0`
- NUCLEO-F446REに接続されているLEDが同時に点滅する信号を送信します

---
## 終了方法

```
$ sudo rmmod signal
$ make clean
```
---

## License
[GNU General Public License v3.0](https://github.com/YukiShigematsu/Robosys1/blob/main/COPYING)
