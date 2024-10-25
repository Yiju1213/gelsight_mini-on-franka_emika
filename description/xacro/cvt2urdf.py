from xacrodoc import XacroDoc

doc = XacroDoc.from_file("hand.urdf.xacro")

# or relative to a ROS package
# e.g., for a file located at some_ros_package/urdf/robot.urdf.xacro:
# doc = XacroDoc.from_package_file("some_ros_package", "urdf/robot.urdf.xacro")

# convert to a string of URDF
# urdf_str = doc.to_urdf_string()

# or write to a file
doc.to_urdf_file("hand.urdf", verbose=True)

print("done")

# or just work with a temp file
# this is useful for working with libraries that expect a URDF *file* (rather
# than a string)
# with doc.temp_urdf_file_path() as path:
  # do stuff with URDF file located at `path`...
  # file is cleaned up once context manager is exited