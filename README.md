# gelsight_mini-on-franka_emika

Robot description package modified from [*franka_ros*](https://github.com/justagist/franka_panda_description) package.

Addtional, Gelsight Mini and Emika finger adapter is added to create the combined URDF. The calculation is conduct through CAD assembly result.

For now, the combined part is only hand+finger+gelsight mini for minimal research requirement.

![example](photo/example.png)

## Usage
- The ready-to-use URDF files are in folder `description/urdf/`:
  - The `hand_origin.urdf` is **auto-generated** through `description/xacro/cv2urdf.py` and represents the original franka_panda.
  - The `hand_gsmini_tacto.urdf` and `hand_gsmini_ros.urdf` is **manual-adjusted** to replace original finger to adapter finger and add gelsight mini. The difference between them is path reference approach for different env.
    - For usage **inside rviz or ros-related env**, please refer to `hand_gsmini_ros.urdf` and replace `package://urdf_rviz_display` in the URDF to your customized package name!
    - For usage **inside tacto-related or pybullet-related env**, please refer to `hand_gsmini_tacto.urdf`, which use relative path as file reference, and add a dummyLink/dummyJoint for safely interact with collision.
- `gsmini_panda_hand.py` is used for controlling `gsmini_panda_hand` in pybullet environment, which is intergrated to TACTO ENV for tactile sensing.

## TODO
- [x] Adjust to adapt in RVIZ ENV
- [x] Adjust to adapt in TACTO/PyBullet ENV
- [ ] Refine the gsmini_panda_hand controller file `gsmini_panda_hand.py` for total control.
