bl_info = {
    'name' : 'Add Triangle',
    'author' : 'Alex Carney',
    'version' : (0, 1, 0),
    'blender' : (2, 77, 0),
    'description' : 'A simple addon which gives the user the ability to add a triangle to the scene',
    'category' : 'Add Mesh'
}

import bpy

class AddTriangle(bpy.types.Operator):
    """
    This operator is responsible for creating a triangle mesh
    and adding it to the scene.
    """
    
    bl_idname = 'add.triangle'
    bl_label = 'Add Triangle'
    
    def execute(self, context):
        """
        Here is where the magic happens
        """
        print("Running!")
        # Get some info about the scene from the context
        scene = context.scene
        cursor_location = scene.cursor_location
        
        # Create a mesh and attach it to an object and link
        # it to the scene
        mesh = bpy.data.meshes.new('TriangleMesh')
        obj = bpy.data.objects.new('Triangle', mesh)
        scene.objects.link(obj)
        
        # Construct the mesh data
        x, y, z = cursor_location
        
        verts = [(x - 0.5, y, z), (x + 0.5, y, z), (x, y + 1, z)]
        faces = [(0,1,2)]
        
        # Calculate the mesh from the data
        mesh.from_pydata(verts, [], faces)
        #                        ^ edges
        
        # IMPORTANT! If you provide face data then edges must be blank and vice versa
        # otherwise there will be trouble!
        
        # Update the mesh
        mesh.update(calc_edges=True)
        
        # Finish
        return {'FINISHED'} 
          

def add_triangle(self, context):
    """
    This function creates a menu item for us to add to the add mesh menu
    for someone to add a square to the scene.
    """
    self.layout.operator(AddTriangle.bl_idname)

def register():
    
    # Register the operator which adds the square to the scene
    bpy.utils.register_class(AddTriangle)
    
    # Add the item to the menu so users can actually call this
    bpy.types.INFO_MT_mesh_add.append(add_triangle)
    
def unregister():
    bpy.utils.unregister_class(AddTriangle)
    
if __name__ == '__main__':
    register()