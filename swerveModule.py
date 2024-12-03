import wpilib
import phoenix6
from wpimath import kinematics, geometry
from math import pi



class SwerveModule: 
    def __init__(self): 
        self.driveMotor = phoenix6.hardware.TalonFX(1) # CAN motor ID 
        
        
        self.m_brake = phoenix6.controls.StaticBrake() # Debug Only. Using this is bad for the motors 

    
    def Debug(self) -> None: 
        self.driveMotor.set_control(self.m_brake)