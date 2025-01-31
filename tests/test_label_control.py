from imgFolder.commands import LabelControl


class TestLabelControl():
	
	def test_prompt_label(self):
		# Arrange
		labeler = LabelControl(imgpath="Pudim")
		true = {"Pudim":"Comida"}

		# Act
		res = labeler._set_label("Comida")
		
		# Assert
		assert(true == res)