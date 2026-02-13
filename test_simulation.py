import math
import pytest
from main import Planet

def test_planet_initialization():
    p = Planet(100, 200, 10, (255, 0, 0), 500)
    assert p.x == 100
    assert p.y == 200
    assert p.radius == 10
    assert p.color == (255, 0, 0)
    assert p.mass == 500

def test_attraction_force():
    p1 = Planet(0, 0, 10, (0,0,0), 10**24)
    p2 = Planet(Planet.AU, 0, 10, (0,0,0), 10**24)
    
    expected_force = Planet.G * (10**24) * (10**24) / (Planet.AU**2)
    
    fx, fy = p1.attraction(p2)
    
    assert math.isclose(fx, expected_force, rel_tol=1e-9)
    assert math.isclose(fy, 0, abs_tol=1e-9)