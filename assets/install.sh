sudo git clone https://github.com/UnityTheCoder/Voxel-2.0 /usr/lib/voxel
python3 -m pip install toml
python3 -m pip install rich
sudo ln -s /usr/lib/voxel/voxel /usr/bin/vxc
sudo chmod +x /usr/bin/vxc
sudo ln -s /usr/lib/voxel/vix /usr/bin/vix
sudo chmod +x /usr/bin/vix
sudo chown -R $(whoami) /usr/lib/voxel/
