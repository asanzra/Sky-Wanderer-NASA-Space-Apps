extends Node # Use the appropriate base class (Node2D, Control, etc.)

@onready var picture = $TextureRect # Reference to the TextureRect node

func _ready():
	DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
	picture.visible = false # Ensure the picture is initially hidden

func _process(delta):
	# Show the picture when the "Space" key is pressed
	if Input.is_action_pressed("ui_accept"): # Default "ui_accept" maps to Space or Enter
		picture.visible = true
	else:
		picture.visible = false
