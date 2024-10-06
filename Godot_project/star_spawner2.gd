extends Node

# Array to store positions and brightness loaded from CSV
var positions: Array[Vector3] = []
var brightness_values: Array[float] = [] # Store brightness values
var star_distance = 40
var star_scale = 0.1

# Texture for the stars (set this to your texture file)
var star_texture: Texture2D

func _ready():
	load_positions_from_csv("res://csv tables/test5000.csv")
	star_texture = load_star_texture("res://sprites/estrella2.png") # Replace with your texture path
	create_galaxy()

# Load positions and brightness from a CSV file
func load_positions_from_csv(file_path: String) -> void:
	var file = FileAccess.open(file_path, FileAccess.READ)
	if file:
		var first_line = file.get_line() # Skip the header line

		while not file.eof_reached():
			var line = file.get_line()
			var data = line.split(",")
			if data.size() == 6: # Updated to handle brightness
				var x = data[2+0].to_float()
				var y = data[2+1].to_float()
				var z = data[2+2].to_float()
				var brightness = data[1].to_float() # Read brightness
				positions.append(Vector3(x, y, z).normalized()*star_distance)
				brightness_values.append(brightness) # Store brightness
		file.close()
		var brightness_max = brightness_values.max()
		var brightness_min = brightness_values.min()
		var brightness_scale = brightness_max - brightness_min
		for i in range(len(brightness_values)):
			brightness_values[i] = (brightness_values[i]-brightness_min)/brightness_scale
	else:
		print("File does not exist: ", file_path)

# Load the star texture
func load_star_texture(texture_path: String) -> Texture2D:
	var texture = load(texture_path) # Load the texture
	if texture is Texture2D:
		return texture
	else:
		print("Error loading texture: ", texture_path)
		return null

# Create stars based on loaded positions
func create_galaxy() -> void:
	for i in range(positions.size()):
		create_star(positions[i], brightness_values[i]) # Pass brightness

# Create a star at a given position with a specific brightness
func create_star(position: Vector3, brightness: float) -> void:
	var star = MeshInstance3D.new()
	star.mesh = create_quad_mesh()
	star.transform.origin = position
	star.material_override = create_billboard_material(brightness) # Pass brightness to material
	add_child(star)
	
# Create a quad mesh to represent a star
func create_quad_mesh() -> Mesh:
	var quad = QuadMesh.new()
	quad.size = Vector2(1.0, 1.0)*star_scale # Set size of the quad, adjust this for larger/smaller stars
	return quad

# Create a billboard material with emission and transparency
func create_billboard_material(brightness: float) -> ShaderMaterial:
	var material = ShaderMaterial.new()

	# Create and set the shader code
	var shader = Shader.new()
	shader.code = """
		shader_type spatial;

		uniform sampler2D texture_albedo;
		uniform float brightness; // Add brightness parameter

		void vertex() {
			// Billboard effect: make the quad face the camera
			MODELVIEW_MATRIX[0] = vec4(1.0, 0.0, 0.0, 0.0);
			MODELVIEW_MATRIX[1] = vec4(0.0, 1.0, 0.0, 0.0);
			MODELVIEW_MATRIX[2] = vec4(0.0, 0.0, 1.0, 0.0);
		}

		void fragment() {
		// Get the texture color
		vec4 tex_color = texture(texture_albedo, UV);
		// Calculate brightness scaling
		float brightness_scale = brightness * 4.0; // Adjust this factor for a stronger effect

		// Set albedo to a value greater than 1 for glowing effect
		ALBEDO = tex_color.rgb * brightness_scale; // Scale the albedo color
		ALPHA = tex_color.a; // Use alpha from texture for transparency

		// Adjust the emission color based on brightness
		vec4 emission_color = vec4(tex_color.rgb * brightness, tex_color.a); // Modify this as needed
		EMISSION = emission_color.rgb * tex_color.a; // Emission based on the alpha of the texture
		}

		render_mode unshaded, depth_draw_opaque, cull_disabled, blend_mix;
	"""

	material.shader = shader # Assign the shader to the material
	material.set_shader_parameter("texture_albedo", star_texture) # Assign the texture to the shader
	material.set_shader_parameter("brightness", brightness) # Set the brightness value
	return material
