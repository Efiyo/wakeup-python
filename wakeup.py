import schedule
import time
from wakeonlan import send_magic_packet

def send_magic_packet_to_pc():
    pc_mac_address = 'xx:xx:xx:xx:xx:xx'
    send_magic_packet(pc_mac_address)
    print(f"Magic packet sent")

schedule.every().day.at("03:00").do(send_magic_packet_to_pc)

while True:
    schedule.run_pending()
    time.sleep(1)
