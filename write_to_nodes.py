from netmiko import Netmiko
import os

file_path = os.path.dirname(os.path.realpath(__file__))

with open(file_path + '/input/node_ids.txt','r') as hostnames:
    iq_device_list = hostnames.readlines()

for device in iq_device_list:
    try:
        net_connect = Netmiko(
            device_type="cisco_xr",
            host=device,
            username='dshaw1',
            password='put_pass',
            global_delay_factor=2,
        )
        with open(file_path + f'/output/{device}.txt','r') as f:
            f2 = f.readlines()
            output = net_connect.send_config_set(f2)
            print(output)
            net_connect.commit()
            net_connect.exit_config_mode()
            net_connect.disconnect()
        print(f"{device} Login:> success push:>success")
    except:
        print(f"{device} Login:> Failed push:> NA")