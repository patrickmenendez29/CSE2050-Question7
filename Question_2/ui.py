from ezgraphics import GraphicsImage, GraphicsWindow

class RecipeUI:

    def __init__(self, gaps, width, height):
        self.gap = gaps
        self.MAX_WIDTH = 720
        self.canvas = self.setup_window(gaps, width, height)
        self.win = GraphicsWindow(width, height)

    def setup_window(self, gaps, width, height):
        canvas = self.win.canvas()
        return canvas

    def layout_ui(self, recipes):
        x, y = 0, 0
        maxY = 0
        for i in range(2, len(recipes) + 1):
            pic = GraphicsImage(recipes.get_image())
            x = x + pic.width() + self.gap
            if x + pic.width() < self.MAX_WIDTH:
                self.canvas.drawImage(x, y, pic)
                self.show_recipe_description(recipes[i], x, y)
            else:
                x = 0
                y = y + maxY + self.gap
                self.canvas.drawImage(x, y, pic)
                self.show_recipe_description(recipes[i], x, y)

    def show_recipe_description(self, recipe, x, y):
        self.canvas.drawText(x, y, f"Name: {recipe.get_name()}")
        self.canvas.drawText(x, y + 10, f"Source: {recipe.get_source()}")
        self.canvas.drawText(x, y + 20, f"Cook time: {recipe.get_cook_time()}")

