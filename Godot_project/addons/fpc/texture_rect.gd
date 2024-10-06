extends TextureRect


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func _input(event):
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		if Global.moved_up == 0:
			NvdaWrapper.say("Visor removed")
			$AnimationPlayer.play("Quitar casco")
			Global.moved_up = 1
		else:
			NvdaWrapper.say("Visor on")
			$AnimationPlayer.play("Poner casco")
			Global.moved_up = 60
	
		
