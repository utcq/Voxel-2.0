# 🔻 Installation

`sh -c $(curl -L https://raw.githubusercontent.com/UnityTheCoder/Voxel-2.0/main/assets/install.sh)`\
``**OR**\
****

```bash
sh -c "sudo rm -r /usr/lib/voxel"
sudo git clone https://github.com/UnityTheCoder/Voxel-2.0 /usr/lib/voxel
python3 -m pip install toml
sh -c "sudo rm /usr/bin/vxc"
sh -c "sudo rm /usr/bin/vix"
sudo ln -s /usr/lib/voxel/voxel /usr/bin/vxc
sudo chmod +x /usr/bin/vxc
sudo ln -s /usr/lib/voxel/vix /usr/bin/vix
sudo chmod +x /usr/bin/vix
```

\
\
`vxc --help`
