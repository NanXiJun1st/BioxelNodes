import re
import bpy
from pathlib import Path
import shutil
from .utils import copy_to_dir, get_all_layers, get_container, get_container_from_selection, get_container_layers
from .nodes import custom_nodes

CLASS_PREFIX = "BIOXELNODES_MT_NODES"


class ReLinkNodes(bpy.types.Operator):
    bl_idname = "bioxelnodes.relink_nodes"
    bl_label = "Relink Nodes to Addon"
    bl_description = "Relink all nodes to addon source"

    def execute(self, context):
        file_name = Path(custom_nodes.nodes_file).name
        for lib in bpy.data.libraries:
            lib_path = Path(bpy.path.abspath(lib.filepath)).resolve()
            lib_name = lib_path.name
            if lib_name == file_name:
                if str(lib_path) != custom_nodes.nodes_file:
                    lib.filepath = custom_nodes.nodes_file

        self.report({"INFO"}, f"Successfully relinked.")

        return {'FINISHED'}


class SaveStagedData(bpy.types.Operator):
    bl_idname = "bioxelnodes.save_staged_data"
    bl_label = "Save Staged Data"
    bl_description = "Save all staged data in this file for sharing"

    save_layer: bpy.props.BoolProperty(
        name="Save Layer VDB Cache",
        default=True,
    )  # type: ignore

    cache_dir: bpy.props.StringProperty(
        name="Cache Directory",
        subtype='DIR_PATH',
        default="//"
    )  # type: ignore

    save_lib: bpy.props.BoolProperty(
        name="Save Node Library File",
        default=True,
    )  # type: ignore

    lib_dir: bpy.props.StringProperty(
        name="Library Directory",
        subtype='DIR_PATH',
        default="//"
    )  # type: ignore

    def execute(self, context):
        if self.save_lib:
            files = []
            for classname in dir(bpy.types):
                if CLASS_PREFIX in classname:
                    cls = getattr(bpy.types, classname)
                    files.append(cls.nodes_file)
            files = list(set(files))

            for file in files:
                file_name = Path(file).name
                # "//"
                lib_dir = bpy.path.abspath(self.lib_dir)

                output_path: Path = Path(lib_dir, file_name).resolve()
                source_path: Path = Path(file).resolve()

                if output_path != source_path:
                    shutil.copy(source_path, output_path)

                for lib in bpy.data.libraries:
                    lib_path = Path(bpy.path.abspath(lib.filepath)).resolve()
                    if lib_path == source_path:
                        blend_path = Path(bpy.path.abspath("//")).resolve()
                        lib.filepath = bpy.path.relpath(
                            str(output_path), start=str(blend_path))

                self.report({"INFO"}, f"Successfully saved to {output_path}")

        if self.save_layer:
            fails = []
            for layer in get_all_layers():
                try:
                    save_layer(layer, self.cache_dir)
                except:
                    fails.append(layer)

            if len(fails) == 0:
                self.report({"INFO"}, f"Successfully saved bioxel layers.")
            else:
                self.report(
                    {"WARNING"}, f"{','.join([layer.name for layer in fails])} fail to save.")

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.invoke_props_dialog(self,
                                                   width=500)
        return {'RUNNING_MODAL'}

    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    def draw(self, context):
        layout = self.layout
        panel = layout.box()
        panel.prop(self, "save_layer")
        panel.prop(self, "cache_dir")
        panel = layout.box()
        panel.prop(self, "save_lib")
        panel.prop(self, "lib_dir")


def save_layer(layer, output_dir):

    pattern = r'\.\d{4}\.'

    # "//"
    output_dir = bpy.path.abspath(output_dir)
    source_dir = bpy.path.abspath(layer.data.filepath)

    source_path: Path = Path(source_dir).resolve()
    is_sequence = re.search(pattern, source_path.name) is not None
    name = layer.name if is_sequence else f"{layer.name}.vdb"
    output_path: Path = Path(output_dir, name, source_path.name).resolve() \
        if is_sequence else Path(output_dir, name).resolve()

    if output_path != source_path:
        copy_to_dir(source_path.parent if is_sequence else source_path,
                    output_path.parent.parent if is_sequence else output_path.parent,
                    new_name=name)

    blend_path = Path(bpy.path.abspath("//")).resolve()

    layer.data.filepath = bpy.path.relpath(
        str(output_path), start=str(blend_path))


class SaveLayers(bpy.types.Operator):
    bl_idname = "bioxelnodes.save_layers"
    bl_label = "Save Layers"
    bl_description = "Save Container Layers to Directory."

    cache_dir: bpy.props.StringProperty(
        name="Layer Directory",
        subtype='DIR_PATH',
        default="//"
    )  # type: ignore

    @classmethod
    def poll(cls, context):
        containers = get_container_from_selection()
        return len(containers) > 0

    def execute(self, context):
        containers = get_container_from_selection()

        if len(containers) == 0:
            self.report({"WARNING"}, "Cannot find any bioxel container.")
            return {'FINISHED'}

        fails = []
        for container in containers:
            for layer in get_container_layers(container):
                try:
                    save_layer(layer, self.cache_dir)
                except:
                    fails.append(layer)

        if len(fails) == 0:
            self.report({"INFO"}, f"Successfully saved bioxel layers.")
        else:
            self.report(
                {"WARNING"}, f"{','.join([layer.name for layer in fails])} fail to save.")

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.invoke_props_dialog(self,
                                                   width=500)
        return {'RUNNING_MODAL'}


class CleanAllCaches(bpy.types.Operator):
    bl_idname = "bioxelnodes.clear_all_caches"
    bl_label = "Clean All Caches in Temp"
    bl_description = "Clean all caches saved in temp"

    def execute(self, context):
        preferences = context.preferences.addons[__package__].preferences
        cache_dir = Path(preferences.cache_dir, 'VDBs')
        try:
            shutil.rmtree(cache_dir)
            self.report({"INFO"}, f"Successfully cleaned caches.")
            return {'FINISHED'}
        except:
            self.report({"WARNING"},
                        "Fail to clean caches, you may do it manually.")
            return {'CANCELLED'}

    def invoke(self, context, event):
        context.window_manager.invoke_confirm(self,
                                              event,
                                              message="All caches will be cleaned, include other project files, do you still want to clean?")
        return {'RUNNING_MODAL'}
