class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    area = self.width*self.height
    return area
  
  def get_perimeter(self):
    return (2*self.width)+(2*self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      star_line = ("*"*self.width + "\n")*self.height
      return star_line
  
  def get_amount_inside(self, othershape):
    result = 0
    if self.width < othershape.width or self.height < othershape.height:
      result = 0
    else: # Compares area of both shapes, after confirming self shape is bigger than othershape in width and height 
      self_area = self.width*self.height
      othershape_area = othershape.width*othershape.height
      result = int(self_area / othershape_area) # int() Rounds number down to nearest integer
    
    return result

  def __str__(self):
    shape_type = ""
    if self.width == self.height:
      shape_type = "Square"
    else:
      shape_type = "Rectangle"
      output = f"{shape_type}(width={self.width}, height={self.height})"
    return output


class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)
    # STILL CONTAINS RECTANGLE LENGTH AND HEIGHT ATTRIBUTES, MUST ADJUST METHODS ACCORDINGLY
  
  def set_side(self, length):
    self.width = length
    self.height = length

  def set_width(self, width):
    self.set_side(width)
  
  def set_height(self, height):
    self.set_side(height)
  
  def __str__(self):
    shape_type = "Square"
    output = f"Square(side={self.width})"
    return output