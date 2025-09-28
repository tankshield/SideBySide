bl_info = {
    "name": "SideBySide",
    "author": "tank shield",
    "version": (1, 1),
    "blender": (4, 5, 0),
    "location": "File > Open New Instance or Open File in New Instance",
    "description": "Launch separate Blender application instances for new or specific .blend files (macOS only).",
    "category": "System",
}

import bpy
import subprocess
from bpy_extras.io_utils import ImportHelper

BLENDER_PATH = "/Applications/Blender.app/Contents/MacOS/Blender"

class SYSTEM_OT_open_new_blank_instance(bpy.types.Operator):
    bl_idname = "system.open_new_blank_instance"
    bl_label = "Open New Blank Blender Instance"
    bl_description = "Launches a new empty Blender window as a separate app process (macOS only)."

    def execute(self, context):
        try:
            subprocess.Popen([BLENDER_PATH])
            self.report({'INFO'}, "New blank Blender instance started.")
        except Exception as e:
            self.report({'ERROR'}, f"Failed: {e}")
        return {'FINISHED'}

class SYSTEM_OT_open_file_new_instance(bpy.types.Operator, ImportHelper):
    bl_idname = "system.open_file_new_instance"
    bl_label = "Open Blender File in New Instance"
    bl_description = "Open a selected .blend file in a new Blender application process (macOS only)."
    filename_ext = ".blend"
    filter_glob: bpy.props.StringProperty(default="*.blend", options={'HIDDEN'})

    def execute(self, context):
        try:
            subprocess.Popen([BLENDER_PATH, self.filepath])
            self.report({'INFO'}, f"Opened new Blender instance with {self.filepath}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to open: {e}")
        return {'FINISHED'}

def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(SYSTEM_OT_open_new_blank_instance.bl_idname, icon='WINDOW')
    layout.operator(SYSTEM_OT_open_file_new_instance.bl_idname, icon='FILE_BLEND')

addon_keymaps = []

def register():
    bpy.utils.register_class(SYSTEM_OT_open_new_blank_instance)
    bpy.utils.register_class(SYSTEM_OT_open_file_new_instance)
    bpy.types.TOPBAR_MT_file.append(menu_func)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        # Shortcut Command+Option+N for blank new instance
        kmi1 = km.keymap_items.new(
            SYSTEM_OT_open_new_blank_instance.bl_idname,
            type='N',
            value='PRESS',
            ctrl=False,
            shift=False,
            alt=True,    # Option key
            oskey=True   # Command key (⌘)
        )
        addon_keymaps.append((km, kmi1))

        # Shortcut Command+Shift+Option+N for open file new instance
        kmi2 = km.keymap_items.new(
            SYSTEM_OT_open_file_new_instance.bl_idname,
            type='N',
            value='PRESS',
            ctrl=False,
            shift=True,
            alt=True,
            oskey=True
        )
        addon_keymaps.append((km, kmi2))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.types.TOPBAR_MT_file.remove(menu_func)

    bpy.utils.unregister_class(SYSTEM_OT_open_file_new_instance)
    bpy.utils.unregister_class(SYSTEM_OT_open_new_blank_instance)

if __name__ == "__main__":
    register()
