class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		def valid(image, row, col):
			if row < 0 or row >= len(image) or col < 0  or col >= len(image[0]):
				return False
			return  True
		
		def dfs(image, row, col, old_color, new_color):
			if not valid(image, row, col):
				return
			
			if image[row][col] != old_color:
				return
			
			image[row][col] = new_color
			
			dfs(image, row - 1, col, old_color, new_color)
			dfs(image, row + 1, col, old_color, new_color)
			dfs(image, row, col - 1, old_color, new_color)
			dfs(image, row, col + 1, old_color, new_color)
			
		# validation
		if image[sr][sc] == newColor:
			return image
		
		dfs(image, sr, sc, image[sr][sc], newColor)
		return image