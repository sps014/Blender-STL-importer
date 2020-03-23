

bl_info = {
    "name": "Fast STL Importer",
    "author": "JM Soler, Sergey Sharybin",
    "blender": (2, 80, 0),
    "location": "File > Import > Fast STL Import",
    "description": "Import STL Mesh",
    "warning": "",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/import_export/curve_svg.html",
    "support": 'OFFICIAL',
    "category": "Import-Export",
}


# To support reload properly, try to access a package var,
# if it's there, reload everything
if "bpy" in locals():
    import importlib
    if "import_svg" in locals():
        importlib.reload(import_svg)


import bpy
from bpy.props import StringProperty
from bpy_extras.io_utils import ImportHelper


class FastImportSTL(bpy.types.Operator,ImportHelper):
    """Load a STL file"""
    bl_idname = "import_scene.stl"
    bl_label = "Import STL"
    bl_options = {'UNDO'}

    filename_ext = ".stl"
    filter_glob: StringProperty(default="*.stl", options={'HIDDEN'})

    def execute(self, context):
        print(self.filepath)
        return {'FINISHED'}
    


def menu_func_import(self, context):
    self.layout.operator(FastImportSTL.bl_idname,
        text="Fast Importer")


def register():
    print("Hello")
    bpy.utils.register_class(FastImportSTL)
   
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(FastImportSTL)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

# NOTES
# - blender version is hardcoded

if __name__ == "__main__":
    register()
