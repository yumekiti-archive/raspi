import RPi.GPIO as GPIO
import time

# モードの指定をする(今回は役割ピン番号)
GPIO.setmode(GPIO.BCM)
# GPIO18pinを入力モードとし、pull up設定とします
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ドアセンサーのon off設定
door_sw = False

# postループ対策
sw_lock = False

while True:
    try:

        # センサーの読み込み
        door_sw = GPIO.input(26)

        if door_sw != sw_lock:

            # on off 確認
            print(door_sw)

        sw_lock = door_sw

        time.sleep(0.50)

    except:
        import traceback
        traceback.print_exc()
        break

# GPIO操作終了
GPIO.cleanup()

# 終わり確認
print("end")