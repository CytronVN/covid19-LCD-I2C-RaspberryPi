import time
import requests
import I2C_LCD_driver

URL = "https://jhucoronavirus.azureedge.net/api/v1/regions/vn.json"

lcd = I2C_LCD_driver.lcd()

new_case = 0
total = 0
prev_total = 0

while True:
    # Request the URL
    resp = requests.get(URL)
    #print(resp.json())
    #print()

    new_case = int(resp.json()["confirmed_cases"]["day"])
    total = resp.json()["confirmed_cases"]["all"]
    print("Thong ke so ca nhiem Covid: {}, Tong so: {}".format(new_case, total))
    # Only display new data on LCD
    if total != prev_total:
        prev_total = total
        print("Hien thi du lieu tren man hinh LCD...")
     # Print on LCD
    lcd.lcd_display_string("Thong ke Covid", 1, 0)
    lcd.lcd_display_string("tai Viet Nam", 2, 0)
  
    time.sleep(4)
    lcd.lcd_clear()

    lcd.lcd_display_string("Ca moi: "+ str(new_case), 1, 0)
    lcd.lcd_display_string("Tong so: "+ str(total), 2, 0)

    time.sleep(120) # Delay for 2 minute
