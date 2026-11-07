class Ghost:
    def __init__(self, x: int, y: int, size: int, speed: list[float], texture: pyray.Texture, color, walls: list[pyray.Rectangle]) -> None:
        """Конструктор применяющий параметры призрака

        :param x: Позиция призрака по x
        :type x: int
        :param y: Позиция призрака по y
        :type y: int
        :param size: Размер призрака в пикселях
        :type size: int
        :param speed: Диапазон скорости призрака
        :type speed: list[float]
        :param texture: Текстура призрака
        :type texture: texture
        :param color: Цвет призрака
        :type color: color
        :param walls: Стены
        :type walls: list[pyray.Rectangle]
        """
        self.x = x
        self.y = y
        self.size = size
        self.speed = round(random.uniform(speed[0], speed[1] - 0.2) / 0.2) * 0.2
        self.texture = texture
        self.color = color
        self.walls = walls
        self.last_step = time.time()
        self.step_cooldown = 0.01
        self.cached_direction = (0,0)
        self.wall_at = (0,0)
    
    def draw(self):
        """Отрисовка призрака
        """
        position = pyray.Vector2(self.x, self.y)
        pyray.draw_texture_ex(self.texture, position, 0, self.size / self.texture.width, self.color)

    def move_towards_player(self, player_x: int, player_y: int):
        """Преследование игрока

        :param player_x: Позиция игрока по x
        :type player_x: int
        :param player_y: Позиция игрока по y
        :type player_y: int
        """
        if self.last_step + self.step_cooldown > time.time():
            return
        dx = player_x - self.x
        dy = player_y - self.y

        if(self.cached_direction!=(0,0) and self.wall_at !=(0,0)):
            new_x = self.x+self.cached_direction[0]
            new_y = self.y+self.cached_direction[1]
        elif(self.wall_at!=(0,0)):
            new_x = self.x+self.wall_at[0]
            new_y = self.y+self.wall_at[1]
            self.wall_at = (0,0)
            self.cached_direction = (0,0)
        else:
            new_x = self.x
            new_y = self.y
            if abs(dx) > abs(dy):
                new_x = self.x + self.speed if dx > 0 else self.x - self.speed
                new_y = self.y
            else:
                new_x = self.x
                new_y = self.y + self.speed if dy > 0 else self.y - self.speed

        is_right = dx>0
        is_above = dy<0

        if not self.collision_with_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y
            if self.cached_direction != (0,0)and not self.collision_with_wall(new_x+self.wall_at[0],new_y-self.wall_at[1]):
                self.cached_direction = (0,0)
        elif self.collision_with_wall(new_x,new_y):
            up = (self.x,self.y-self.speed)
            down= (self.x,self.y+self.speed)
            left=(self.x-self.speed,self.y)
            right=(self.x+self.speed,self.y)
            if is_above and is_right and self.collision_with_wall(*up) or self.collision_with_wall(*down)  and not self.collision_with_wall(*right) and self.cached_direction==(0,0):
                self.wall_at = (0,self.speed) if self.collision_with_wall(*down) else (0,-self.speed)
                self.cached_direction = (self.speed,0)
            elif is_above and not is_right and self.collision_with_wall(*up) or self.collision_with_wall(*down) and not self.collision_with_wall(*left) and self.cached_direction==(0,0):
                self.wall_at = (0,self.speed) if self.collision_with_wall(*down) else (0,-self.speed)
                self.cached_direction = (-self.speed,0)
            elif not is_above and is_right  and self.collision_with_wall(*up) or self.collision_with_wall(*down) and not self.collision_with_wall(*right) and self.cached_direction==(0,0):
                self.wall_at = (0,self.speed) if self.collision_with_wall(*down) else (0,-self.speed)
                self.cached_direction = (self.speed,0)
            elif not is_above and not is_right and self.collision_with_wall(*up) or self.collision_with_wall(*down) and not self.collision_with_wall(*right) and self.cached_direction==(0,0):
                self.wall_at = (0,self.speed) if self.collision_with_wall(*down) else (0,-self.speed)
                self.cached_direction = (-self.speed,0)    
            elif is_above and not is_right and self.collision_with_wall(*left) or self.collision_with_wall(*right) and not self.collision_with_wall(*up) and self.cached_direction==(0,0):
                self.wall_at = (self.speed,0) if self.collision_with_wall(*right) else (-self.speed,0)
                self.cached_direction = (0,-self.speed)  
            elif is_above and is_right and self.collision_with_wall(*left)or  self.collision_with_wall(*right)  and not self.collision_with_wall(*up) and self.cached_direction==(0,0):
                self.wall_at = (self.speed,0) if self.collision_with_wall(*right) else (-self.speed,0)
                self.cached_direction = (0,-self.speed)  
            elif not is_above and is_right and self.collision_with_wall(*left) or  self.collision_with_wall(*right)  and not self.collision_with_wall(*down) and self.cached_direction==(0,0):
                self.wall_at = (self.speed,0) if self.collision_with_wall(*right) else (-self.speed,0)
                self.cached_direction = (0,self.speed)  
            elif not is_above and not is_right and self.collision_with_wall(*left) or  self.collision_with_wall(*right) and not self.collision_with_wall(*down) and self.cached_direction==(0,0):
                self.wall_at = (self.speed,0) if self.collision_with_wall(*right) else (-self.speed,0)
                self.cached_direction = (0,self.speed)  

        self.last_step = time.time()

    def collision_with_wall(self, x, y):
        """Коллизии со стеной

        :param x: Координата призрака по x в данный момент
        :type x: int
        :param y: Координата призрака по y в данный момент
        :type y: int
        """
        ghost_rect = pyray.Rectangle(x, y, self.size, self.size)
        for wall in self.walls:
            if pyray.check_collision_recs(ghost_rect, wall):
                return True
        return False
        
    def collision_with_player(self, player_x, player_y, player_size):
        """Коллизии с игроком

        :param player_x: Позиция игрока по x в данный момент
        :type player_y: int
        :param player_y: Позиция игрока по y в данный момент
        :type player_x: int
        :param player_size: Размер игрока
        :type player_size: int
        """
        ghost_rect = pyray.Rectangle(self.x, self.y, self.size, self.size)
        player_rect = pyray.Rectangle(player_x, player_y, player_size, player_size)
        return pyray.check_collision_recs(ghost_rect, player_rect)