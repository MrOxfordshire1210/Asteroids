import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x ,y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shot_cooldown = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface):
        return pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt: float) -> float:
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            return self.rotate(-dt)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        if keys[pygame.K_s]:
            return self.move(-dt)
        if keys[pygame.K_w]:
            return self.move(dt)
        if keys[pygame.K_SPACE]:        
            return self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        return self.position
    
    def shoot(self):
        if self.shot_cooldown > 0:
            pass
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            bullet_direction = pygame.Vector2(0, 1)
            rotated_direction = bullet_direction.rotate(self.rotation)
            bullet.velocity = rotated_direction * PLAYER_SHOOT_SPEED