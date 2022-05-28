# Proxy Configuration

## Author

|    **Full Name**     |         **Email**          |              **GitHub**               |
| :------------------: | :------------------------: | :-----------------------------------: |
| Ariel Plasencia Díaz | arielplasencia00@gmial.com | [ArielXL](https://github.com/ArielXL) |

## About

This is a script which configures removes the hassle of configuring proxy manually by supporting system wide proxy-configuration. It is kept as simple as possible. No extra library other than the one that comes with python3 is used.

Currently tested on ubuntu 14.04, 16.04, 18.04, 20.04.

There are four options:

1. Set proxy : Takes input from the user and modifies the required files.
2. Remove proxy : Remove any proxy settings if present in the files.
3. View Proxy : Displays the current proxy settings if there are any.
4. Restore default : Restores to the state before running this script for the first time.

## Run 

```bash
chmod +x proxy.py
sudo ./proxy.py
```

## Support
```text
Currently it modifies the following files
1)/etc/apt/apt.conf
2)/etc/environment
3)/etc/bash.bashrc
```

