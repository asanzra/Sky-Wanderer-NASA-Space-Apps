extends Node3D

# Number of stars to generate
var star_count: int = 100
# Range within which stars are randomly placed
var range: Vector3 = Vector3(100., 100., 100.)

# Called when the node enters the scene tree for the first time
func _ready():
	randomize()  # Ensures random positions for the stars
	create_stars()

# Function to create glowing stars
func create_stars():
	for i in star_count:
		var star = MeshInstance3D.new()
		
		# Create a sphere mesh for the star
		var sphere_mesh = SphereMesh.new()
		sphere_mesh.radius = 0.5  # Adjust the size of the stars
		star.mesh = sphere_mesh

		# Create a glowing material
		var material = StandardMaterial3D.new()
		material.emission_enabled = true
		material.emission = Color(1.0, 1.0, 1.0)  # White glowing light
		material.emission_energy = 1.5  # Adjust the glow intensity
		star.material_override = material

		# Set the star's position randomly within the range
		var random_position = Vector3(
			randf_range(-range.x, range.x),
			randf_range(-range.y, range.y),
			randf_range(-range.z, range.z)
		)
		star.position = random_position

		# Add the star as a child of the current node
		add_child(star)
