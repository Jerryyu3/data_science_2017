我的程式包含三個function，分別為bar_line_plot(datas, class_name, keys, if_bar)、pie_plot(datas, class_name, keys)跟main()

先從main開始，我利用ssl.SSLContext()這個function，使得下一行的urllib.request.urlopen()可以拿到https的網址所儲存的檔案內容，並用readlines()讀檔案
接著，將各種不同class的data儲存到class_data這個變數，keys為小的class name(如junior high)，values為一個list，儲存這個class的所有數值資料(男vs女、有/無吸菸)
同時，將三個大class下的小class們的名稱存到small_class_name這個list，以及將讀入順序存進big_class_order中，方便在parse argument的時候，找到正確對應的小class
最後進入parse argument，把augument一個一個讀進來，並用if-elif函數把class_data中跟此argument有關的資料拿出來整理成一個二維的list，並呼叫相對應的function畫圖

bar_line_plot吃四個參數，datas為欲畫出的圖所屬的大class(如Education level)之所有資料、class_name為欲畫的大class名稱、keys為各個小class的名稱(如junior)、if_bar判斷要畫的是bar chart 還是line chart
bar_line_plot先把men、women、total的抽菸人數計算出來，接著依照欲畫的chart type，呼叫相對應的function畫出圖，並把標題、坐標軸的label等資訊放上去，針對bar chart用autolabel_bar將數值印在圖上，最後便可顯示出

pie_plot的部分吃三個參數，內容與bar_line_plot的前三個參數一樣
pie_plot先計算出每個小class中抽菸的人數，再計算比例，接著依樣把標題、不同class的label等資訊放上去，最後把圖印出來


