extends Node


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$Label.visible_ratio = 0
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
