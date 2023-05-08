from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

scenario_1_local = 'http://localhost:3000/?v=-250.17116762774398,-114.67919463709383,250.62557403459047,109.37518092954436&df=true&kiosk=true&l=Coastlines_15m,OrbitTracks_Terra_Descending,MODIS_Terra_CorrectedReflectance_TrueColor&lg=true'
scenario_2_local = 'http://localhost:3000/?v=-245.94859690671547,-117.45443360228612,249.20837839391078,104.0767339931503&df=true&kiosk=true&l=Coastlines_15m(opacity=0.63),VIIRS_SNPP_DayNightBand_At_Sensor_Radiance&lg=true'
scenario_3_local = 'http://localhost:3000/?v=-223.38671531740192,-111.23416482365595,252.6798741684782,101.75604370153731&z=4&ics=true&ici=5&icd=10&kiosk=true&df=true&eic=sa&l=Reference_Features_15m,GOES-West_ABI_GeoColor,GOES-East_ABI_GeoColor,VIIRS_SNPP_CorrectedReflectance_TrueColor(opacity=0.61)&lg=true'
scenario_4_local = 'http://localhost:3000/?v=-250.11417226328018,-109.56950433055823,250.18517918522548,114.26234092687216&df=true&kiosk=true&l=Coastlines_15m,VIIRS_SNPP_Thermal_Anomalies_375m_Day,VIIRS_SNPP_CorrectedReflectance_TrueColor&lg=true'
scenario_5_local = 'http://localhost:3000/?v=-243.27471729873875,-101.84591344837116,205.18810596457044,98.79448508453643&df=true&kiosk=true&l=IMERG_Precipitation_Rate,Land_Mask&lg=false'
scenario_6_local = 'http://localhost:3000/?v=-249.0656215906355,-115.52476681117328,248.89235122405506,107.25955540123256&df=true&kiosk=true&l=Coastlines_15m(opacity=0.71),GHRSST_L4_MUR_Sea_Surface_Temperature(palette=rainbow_1)&lg=true'
scenario_7_local = 'http://localhost:3000/?v=-250.02535487803547,-114.4840680358938,251.1027632513897,109.71856398138546&df=true&kiosk=true&l=Coastlines_15m,MODIS_Aqua_L3_Land_Surface_Temp_Daily_Day,MODIS_Aqua_CorrectedReflectance_TrueColor(opacity=0.7)&lg=true'
scenario_8_local = 'http://localhost:3000/?v=-9215416.788865805,-4212995.281243633,9489665.699466601,4155580.686192584&p=arctic&df=true&kiosk=true&eic=da&l=Land_Mask,AMSRU2_Sea_Ice_Concentration_12km(palette=blue_6)&lg=true'

scenario_1_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-250.17116762774398,-114.67919463709383,250.62557403459047,109.37518092954436&df=true&kiosk=true&l=Coastlines_15m,OrbitTracks_Terra_Descending,MODIS_Terra_CorrectedReflectance_TrueColor&lg=true'
scenario_2_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-245.94859690671547,-117.45443360228612,249.20837839391078,104.0767339931503&df=true&kiosk=true&l=Coastlines_15m(opacity=0.63),VIIRS_SNPP_DayNightBand_At_Sensor_Radiance&lg=true'
scenario_3_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-223.38671531740192,-111.23416482365595,252.6798741684782,101.75604370153731&z=4&ics=true&ici=5&icd=10&kiosk=true&df=true&eic=sa&l=Reference_Features_15m,GOES-West_ABI_GeoColor,GOES-East_ABI_GeoColor,VIIRS_SNPP_CorrectedReflectance_TrueColor(opacity=0.61)&lg=true'
scenario_4_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-250.11417226328018,-109.56950433055823,250.18517918522548,114.26234092687216&df=true&kiosk=true&l=Coastlines_15m,VIIRS_SNPP_Thermal_Anomalies_375m_Day,VIIRS_SNPP_CorrectedReflectance_TrueColor&lg=true'
scenario_5_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-243.27471729873875,-101.84591344837116,205.18810596457044,98.79448508453643&df=true&kiosk=true&l=IMERG_Precipitation_Rate,Land_Mask&lg=false'
scenario_6_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-249.0656215906355,-115.52476681117328,248.89235122405506,107.25955540123256&df=true&kiosk=true&l=Coastlines_15m(opacity=0.71),GHRSST_L4_MUR_Sea_Surface_Temperature(palette=rainbow_1)&lg=true'
scenario_7_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-250.02535487803547,-114.4840680358938,251.1027632513897,109.71856398138546&df=true&kiosk=true&l=Coastlines_15m,MODIS_Aqua_L3_Land_Surface_Temp_Daily_Day,MODIS_Aqua_CorrectedReflectance_TrueColor(opacity=0.7)&lg=true'
scenario_8_SIT = 'https://worldview.sit.earthdata.nasa.gov/?v=-9215416.788865805,-4212995.281243633,9489665.699466601,4155580.686192584&p=arctic&df=true&kiosk=true&eic=da&l=Land_Mask,AMSRU2_Sea_Ice_Concentration_12km(palette=blue_6)&lg=true'



# Replace the following with the 4 pannels you want to test
urls = [scenario_5_SIT, scenario_6_SIT, scenario_7_SIT, scenario_8_SIT]

options = Options()
options.headless = False

# Get screen size
screen_width = int(os.environ.get("WIDTH", 1920))
screen_height = int(os.environ.get("HEIGHT", 1080))

# Create browser instances
browsers = [webdriver.Chrome(options=options) for _ in range(4)]

# Set window positions and sizes for each instance
window_width = screen_width // 2
window_height = screen_height // 2
for i, browser in enumerate(browsers):
    browser.set_window_position(window_width * (i % 2), window_height * (i // 2))
    browser.set_window_size(window_width, window_height)

# Refresh the pages every 90 seconds
while True:
    for browser, url in zip(browsers, urls):
        browser.get(url)
    time.sleep(90)
