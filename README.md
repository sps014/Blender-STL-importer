# Blender fast STL importer plugin
 
With Memory mapped file Blender can now import Files with massive vertex information

#### Build Instruction
1. Install Visual Studio with C++ workload 
2. On other OS use Mingw toolchain
3. Use Cmake to build the project
```
blender [<scene.blend>] -P mesh_readply.py -- myfile.ply
```
