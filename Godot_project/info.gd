extends Node # Use the appropriate base class (Node2D, Control, etc.)

@onready var picture = $TextureRect # Reference to the TextureRect node

func _ready():
	DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
	picture.visible = false # Ensure the picture is initially hidden

func _process(delta):
	# Show the picture when the "Space" key is pressed
	if Input.is_action_pressed("ui_accept"): # Default "ui_accept" maps to Space or Enter
		NvdaWrapper.say("You have selected star Kepler-737. 
		This star is part of Constellation seen from the Earth: Cygnus.
		It is 673 light years from Earth. It has a Stellar Mass and Stellar Radii equivalent to 0.51 and 0.48 Solar units, respectively
		Moreover, its habitable zone ranges from 0.24-0.50 Astronomical Units.")
		picture.visible = true
	else:
		picture.visible = false
