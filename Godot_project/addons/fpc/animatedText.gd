extends Node
var camera = get_node("Head/Camera")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$Label.visible_ratio = 0
	NvdaWrapper.say("You are a space explorer and you find yourself on top of an unknown planet. You have a visor on, where 
	the following text is displayed:
		Welcome to Sky Wanderer. Your job is to explore the galaxy.
		From the NASA Base Station, we will guide you through your journey.
		First, you will visit planet XYZ.
		Get ready for take-off...
	
---Press LEFT MOUSE BUTTON to close the visor, then SPACE to select a celestial and know more information about it---")
	$AnimationPlayer.play("show")
	#$Countdown2.queue("show")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
	#if $Label.visible_ratio != 1:
		#$AnimationPlayer.play("show")
		#$Countdown2.queue("show")
	#if $Label.visible_ratio == 1:
		#$Label.hide()


func _input(event):
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		$Label.hide()
		#$Countdown2.play("show")
