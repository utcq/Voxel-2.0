sh -c "sudo rm -r /usr/lib/voxel"
sudo git clone https://github.com/UnityTheCoder/Voxel-2.0 /usr/lib/voxel
sh -c "sudo rm /usr/bin/vxc"
sudo ln -s /usr/lib/voxel/voxel /usr/bin/vxc
sudo chmod +x /usr/bin/vxc
