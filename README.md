# Turn Lefter

左折だけで目的地に行きたい

## OSMnxとは？
OSMnx is pronounced as the initialism: “oh-ess-em-en-ex”. It is built on top of NetworkX and GeoPandas, and interacts with OpenStreetMap APIs to:

（訳）
OSMnx は、頭文字をとって「オーエスエムエンエクス」と発音されます。 NetworkX と GeoPandas をベースに構築されており、OpenStreetMap API と連携して次の操作を行います。

https://osmnx.readthedocs.io/en/stable/getting-started.html#introducing-osmnx


### OpenStreetMap APIとは？
https://www.openstreetmap.org/about

オープンライセンスで使える地図。世界中でメンテナンスされている。

日本のコミュニティもあるようです
https://openstreetmap.jp/node/762

### foliumとは？
`leaflet.js` というJavaScriptのライブラリをPythonから使えるようにしたライブラリ
OSMnxからも使えるが、v2以降はdeprecated

## インストール

```bash
$ pip install osmnx matplotlib jupyterlab
$ pip install networkx geopandas folium
$ pip install scikit-learn
$ jupyter lab
```